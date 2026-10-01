"""Full 40-die V-die stack: inter-die water (with/without Cu pillars) vs top-side cold plate.

Geometry (mm):  x = stacking axis, y = die width (flow direction), z = die height.
  * 40 Si dies, 11 (y) x 11 (z) x 0.200 (x); 39 gaps of 0.175 mm. Stack 14.825 mm in x.
  * Si interposer 0.775 mm thick under the stack (z < 0). Truncated to the stack
    footprint (14.825 x 11 mm) so the Region equals the model bounding box
    (lateral spreading beyond the footprint is neglected). Interposer bottom adiabatic.
  * Die bottom edges sit directly on the interposer (ideal thermal contact).
Loads:
  * Every die: 3 W uniform.
  * Even-index dies (0, 2, ..., 38; 20 "active" dies): extra I/O hotspot,
    +50 W/cm2 over 0.3 (y) x 0.3 (z) mm at the bottom edge, y-centred, full die
    thickness -> +0.045 W per active die. Total = 120.9 W.
Cases (--case):
  empty   : water in all 39 gaps, uniform inlet velocity on every gap (ideal
            manifold) at y = 0, pressure outlet at y = 11. Gap tops/bottoms sealed.
  pillar  : as empty + Cu pillars (d 75 um, p 150 um, staggered) in a 1.2 x 1.2 mm
            patch around the I/O hotspot in every gap (60 pillars/gap, 2,340 total).
  topside : no coolant; gaps filled with stagnant air (flow disabled); die top edges
            (z = 11 mm) held at 25 C (ideal cold plate, zero TIM resistance).
Physics: steady, laminar, constant-property water, 25 C inlet, conjugate conduction.
Output: Runs/study_40die/results_40die.csv, per-die CSV per case.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
import traceback
from pathlib import Path

from ansys.aedt.core import Icepak

ROOT = Path(__file__).resolve().parent.parent / "Runs" / "study_ndie"
N_DIE = 40  # overridden by --ndie
T_DIE = 0.200
GAP = 0.175
PITCH_X = T_DIE + GAP
W = 11.0          # y
H = 11.0          # z
T_INT = 0.775
P_DIE = 3.0
HS = 0.300
HS_EXTRA_W = 50.0 * 1e-2 * HS * HS   # 50 W/cm2 over 0.09 mm2
T_IN = 25.0
WATER = dict(k=0.607, rho=997.0, cp=4181.3, mu=0.00089)
PIL_D, PIL_P = 0.075, 0.150
PATCH = 1.2
MAX_IT = 500

FIELDS = ["case", "status", "velocity_m_s", "total_power_W", "n_pillars", "cells",
          "iterations", "Tmax_C", "T_hotspot_max_C", "Tmax_active_mean_C",
          "Tmax_idle_mean_C", "dT_adjacent_max_C", "Tmax_center_die_C", "Tmax_end_die_C",
          "dp_Pa", "pumping_power_W", "Tmax_interposer_C", "error"]


def _num(v):
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, (list, tuple)):
        return _num(v[0])
    return float(str(v).split()[0])


def _stat(r, *keys):
    for k in keys:
        if k in r:
            return _num(r[k])
    raise RuntimeError(f"{keys} not in {r}")


def _faces_at(obj, axis, target, tol=1e-5):
    return [f.id for f in obj.faces if abs(float(f.center[axis]) - target) <= tol]


def die_x0(i):
    return i * PITCH_X


def _sheet(app, x0, y, name, order):
    s = app.modeler.create_rectangle(orientation="ZX", origin=[x0, y, 0.0],
                                     sizes=order, name=name)
    xs = [float(v.position[0]) for v in s.vertices]
    zs = [float(v.position[2]) for v in s.vertices]
    ok = (math.isclose(min(xs), x0, abs_tol=1e-6) and math.isclose(max(xs), x0 + GAP, abs_tol=1e-6)
          and math.isclose(max(zs), H, abs_tol=1e-6))
    return s, ok


def build(app, case):
    dies, hots = [], []
    for i in range(N_DIE):
        d = app.modeler.create_box([die_x0(i), 0, 0], [T_DIE, W, H], f"Die_{i:02d}", "silicon")
        if i % 2 == 0:
            h = app.modeler.create_box([die_x0(i), W / 2 - HS / 2, 0], [T_DIE, HS, HS],
                                       f"IO_Hot_{i:02d}", "silicon")
            if not app.modeler.subtract(d, h, keep_originals=True):
                raise RuntimeError(f"hotspot subtract {i}")
            hots.append(h)
        dies.append(d)
    stack_x = die_x0(N_DIE - 1) + T_DIE
    inter = app.modeler.create_box([0, 0, -T_INT], [stack_x, W, T_INT], "Interposer", "silicon")

    pillars = []
    if case == "pillar":
        y0 = W / 2 - PATCH / 2
        rows = round(PATCH / PIL_P)
        first = []
        x_gap0 = die_x0(0) + T_DIE
        for r in range(rows):
            y = y0 + (r + 0.5) * PIL_P
            zs = ([(c + 0.5) * PIL_P for c in range(rows)] if r % 2 == 0
                  else [c * PIL_P for c in range(1, rows)])
            for z in zs:
                p = app.modeler.create_cylinder("X", [x_gap0, y, z], PIL_D / 2, GAP,
                                                name=f"CuPillar_r{r}_z{int(round(z * 1000))}",
                                                material="copper")
                if not p:
                    raise RuntimeError("pillar creation failed")
                first.append(p.name)
        ok, _ = app.modeler.duplicate_along_line(first, [PITCH_X, 0, 0], clones=N_DIE - 1)
        if not ok:
            raise RuntimeError("duplicate_along_line failed")
        pillars = [n for n in app.modeler.object_names if n.startswith("CuPillar")]
        if len(pillars) != len(first) * (N_DIE - 1):
            raise RuntimeError(f"pillar count {len(pillars)} != {len(first) * (N_DIE - 1)}")

    app.modeler.change_region_padding(["0"] * 6, padding_type=["Percentage Offset"] * 6,
                                      direction=["+X", "-X", "+Y", "-Y", "+Z", "-Z"])
    region = app.modeler["Region"]
    bb = [float(v) for v in region.bounding_box]
    exp = [0, 0, -T_INT, stack_x, W, H]
    if not all(math.isclose(a, b, abs_tol=1e-5) for a, b in zip(bb, exp)):
        raise RuntimeError(f"Region bbox {bb} != {exp}")
    return dies, hots, inter, pillars, region


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=["empty", "pillar", "topside"], required=True)
    ap.add_argument("--ndie", type=int, default=10)
    ap.add_argument("--mesh", choices=["manual", "manual_nomlm", "auto3", "stackregion"], default="manual_nomlm")
    ap.add_argument("--autores", type=int, default=3)
    ap.add_argument("--ratio", default="5")
    ap.add_argument("--localdx", type=float, default=0.0, help=">0: manual local region cell size (mm)")
    ap.add_argument("--vel", type=float, default=0.5)
    ap.add_argument("--res", type=int, default=0, help="global auto-mesh resolution 1..5; 0 = manual sizes")
    ap.add_argument("--dx", type=float, default=0.025, help="manual max cell size along stack axis (mm)")
    ap.add_argument("--gapcells", type=int, default=7, help="MinElementsInGap (cells across each gap)")
    ap.add_argument("--dyz", type=float, default=0.25, help="manual max cell size in die plane (mm)")
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    global N_DIE
    N_DIE = a.ndie
    ROOT.mkdir(parents=True, exist_ok=True)
    name = f"vdie{a.ndie}_{a.case}_{a.mesh}" + (f"{a.autores}" if a.mesh == "auto3" else f"_r{a.ratio}_l{a.localdx*1000:.0f}") + (f"_v{a.vel:g}".replace(".", "p") if a.case != "topside" else "") \
        + (f"_r{a.res}" if a.res else f"_man{a.dx*1000:.0f}um_gc{a.gapcells}") + (f"_{a.tag}" if a.tag else "")
    cdir = ROOT / name
    n = 2
    while (cdir / f"{cdir.name}.aedt").exists():
        cdir = ROOT / f"{name}_{n}"
        n += 1
    cdir.mkdir(parents=True)
    proj = cdir / f"{cdir.name}.aedt"

    total_p = N_DIE * P_DIE + (N_DIE // 2) * HS_EXTRA_W
    row = {k: "" for k in FIELDS}
    row.update(case=cdir.name, velocity_m_s=a.vel if a.case != "topside" else "", total_power_W=total_p)
    app = None
    try:
        app = Icepak(project=str(proj), design="V40", non_graphical=True, new_desktop=True)
        app.modeler.model_units = "mm"
        app.edit_design_settings(ambient_temperature=T_IN, radiation_temperature=T_IN)
        for nm, props in (("silicon", (148, 2330, 700)), ("copper", (398, 8960, 385))):
            m = app.materials[nm]
            m.thermal_conductivity, m.mass_density, m.specific_heat = map(str, props)
            m.update()

        dies, hots, inter, pillars, region = build(app, a.case)
        row["n_pillars"] = len(pillars)
        f_hot = HS * HS / (W * H)
        for i, d in enumerate(dies):
            p = P_DIE * (1 - f_hot) if i % 2 == 0 else P_DIE
            app.assign_solid_block(object_name=d.name, boundary_name=f"P_{d.name}",
                                   power_assignment=f"{p:.12g}W")
        for h in hots:
            app.assign_solid_block(object_name=h.name, boundary_name=f"P_{h.name}",
                                   power_assignment=f"{P_DIE * f_hot + HS_EXTRA_W:.12g}W")

        setup = app.create_setup(name="SteadyState", setup_type="IcepakSteadyState")
        setup.props["Convergence Criteria - Max Iterations"] = MAX_IT
        inlets, outlets = [], []
        if a.case == "topside":
            top = []
            for d in dies:
                top += _faces_at(d, 2, H)
            if len(top) != N_DIE:
                raise RuntimeError(f"top faces {len(top)}")
            app.assign_source(top, thermal_condition="Fixed Temperature",
                              assignment_value=f"{T_IN}cel", boundary_name="ColdPlate_Top")
            setup.props["Include Flow"] = False
        else:
            w = app.materials["water"]
            w.thermal_conductivity = str(WATER["k"]); w.mass_density = str(WATER["rho"])
            w.specific_heat = str(WATER["cp"]); w.viscosity = str(WATER["mu"]); w.update()
            region.material_name = "Water"
            order = None
            for g in range(N_DIE - 1):
                x0 = die_x0(g) + T_DIE
                for y, lst, tag in ((0.0, inlets, "In"), (W, outlets, "Out")):
                    cands = [order] if order else [[H, GAP], [GAP, H]]
                    for o in cands:
                        s, ok = _sheet(app, x0, y, f"{tag}_{g:02d}", o)
                        if ok:
                            order = o
                            lst.append(s)
                            break
                        app.modeler.delete(s.name)
                    else:
                        raise RuntimeError(f"sheet {tag}_{g}")
            app.assign_velocity_free_opening([s.name for s in inlets], boundary_name="Coolant_Inlet",
                                             temperature=f"{T_IN}cel",
                                             velocity=["0m_per_sec", f"{a.vel}m_per_sec", "0m_per_sec"])
            app.assign_pressure_free_opening([s.name for s in outlets], boundary_name="Coolant_Outlet",
                                             temperature=f"{T_IN}cel", pressure=0.0)
            setup.props["Flow Regime"] = "Laminar"
            setup.props["Discretization Scheme - Momentum"] = "Second"

        gm = app.mesh.global_mesh_region
        # Local refinement: hotspots + the few pillars at the patch extremes, so the
        # sub-region bounding box spans the whole pillar patch without passing hundreds
        # of objects (AEDT dropped the connection with 545 objects; a model box
        # intersected the dies at validation).
        local = [h.name for h in hots]
        if pillars:
            bbs = {p: [float(v) for v in app.modeler[p].bounding_box] for p in pillars}
            ext = set()
            for k in range(6):
                pick = (min if k < 3 else max)(bbs, key=lambda p: bbs[p][k])
                ext.add(pick)
            local += sorted(ext)
        if a.mesh == "auto3":
            gm.settings["MeshRegionResolution"] = a.autores
            if not gm.update():
                raise RuntimeError("global mesh update failed")
            app.mesh.assign_mesh_region(assignment=local, level=4, name="Fine_Local")
        elif a.mesh in ("manual", "manual_nomlm"):
            gm.manual_settings = True
            gm.settings["MaxElementSizeX"] = f"{a.dx}mm"
            gm.settings["MaxElementSizeY"] = f"{a.dyz}mm"
            gm.settings["MaxElementSizeZ"] = f"{a.dyz}mm"
            gm.settings["MinElementsInGap"] = str(a.gapcells)
            gm.settings["MinElementsOnEdge"] = "2"
            gm.settings["MaxSizeRatio"] = a.ratio
            if a.mesh == "manual_nomlm":
                gm.settings["EnableMLM"] = False
            if not gm.update():
                raise RuntimeError("global mesh update failed")
            lr = app.mesh.assign_mesh_region(assignment=local, level=4, name="Fine_Local")
            if a.localdx > 0:
                lr.manual_settings = True
                for k in ("MaxElementSizeX", "MaxElementSizeY", "MaxElementSizeZ"):
                    lr.settings[k] = f"{a.localdx}mm"
                lr.settings["EnableMLM"] = False
                lr.settings["MaxSizeRatio"] = a.ratio
                if not lr.update():
                    raise RuntimeError("local mesh update failed")
        else:  # stackregion: manual sub-region over all dies (and local objects)
            gm.settings["MeshRegionResolution"] = 2
            gm.update()
            mr = app.mesh.assign_mesh_region(assignment=[d.name for d in dies], level=4,
                                             name="Stack_Manual")
            mr.manual_settings = True
            mr.settings["MaxElementSizeX"] = f"{a.dx}mm"
            mr.settings["MaxElementSizeY"] = f"{a.dyz}mm"
            mr.settings["MaxElementSizeZ"] = f"{a.dyz}mm"
            mr.settings["MinElementsInGap"] = str(a.gapcells)
            mr.settings["EnableMLM"] = False
            if not mr.update():
                raise RuntimeError("stack mesh region update failed")
        setup.update()
        app.save_project()

        # Read back the cold-plate boundary type (AEDT silently changed it once).
        if a.case == "topside":
            txt = proj.read_text(errors="ignore")
            blk = txt[txt.find("$begin 'ColdPlate_Top'"):txt.find("$end 'ColdPlate_Top'")]
            if "Fixed Temperature" not in blk:
                raise RuntimeError(f"Cold plate boundary not stored as Fixed Temperature:\n{blk}")

        if app.analyze(setup=setup.name) is False:
            msgs = []
            for sev in (0, 1, 2, 3):
                for pn, dn in ((app.project_name, app.design_name), (app.project_name, ""), ("", "")):
                    try:
                        msgs += [f"[{sev}|{pn}|{dn}] {m}" for m in app.odesktop.GetMessages(pn, dn, sev)]
                    except Exception as exc:
                        msgs.append(f"GetMessages error {exc}")
            (cdir / "aedt_messages.txt").write_text("\n".join(msgs), encoding="utf-8")
            raise RuntimeError("analyze returned False; see aedt_messages.txt")

        per = []
        for i, d in enumerate(dies):
            r = app.post.evaluate_object_quantity(object_name=d.name, quantity_name="Temperature", volume=True)
            tmax, tavg = _stat(r, "Max", "max"), _stat(r, "Mean", "mean")
            if i % 2 == 0:
                h = hots[i // 2]
                rh = app.post.evaluate_object_quantity(object_name=h.name, quantity_name="Temperature", volume=True)
                thot = _stat(rh, "Max", "max")
                tmax = max(tmax, thot)
            else:
                thot = ""
            per.append(dict(die=i, active=(i % 2 == 0), Tmax_C=tmax, Tavg_C=tavg, T_hotspot_C=thot))
        with (cdir / "per_die.csv").open("w", newline="") as fh:
            wr = csv.DictWriter(fh, fieldnames=list(per[0].keys()))
            wr.writeheader(); wr.writerows(per)
        ri = app.post.evaluate_object_quantity(object_name=inter.name, quantity_name="Temperature", volume=True)
        act = [p["Tmax_C"] for p in per if p["active"]]
        idle = [p["Tmax_C"] for p in per if not p["active"]]
        row.update(Tmax_C=max(p["Tmax_C"] for p in per),
                   T_hotspot_max_C=max(p["T_hotspot_C"] for p in per if p["active"]),
                   Tmax_active_mean_C=sum(act) / len(act), Tmax_idle_mean_C=sum(idle) / len(idle),
                   dT_adjacent_max_C=max(abs(per[i]["Tmax_C"] - per[i + 1]["Tmax_C"]) for i in range(N_DIE - 1)),
                   Tmax_center_die_C=per[N_DIE // 2]["Tmax_C"], Tmax_end_die_C=max(per[0]["Tmax_C"], per[-1]["Tmax_C"]),
                   Tmax_interposer_C=_stat(ri, "Max", "max"))
        if a.case != "topside":
            pin = app.post.evaluate_faces_quantity(faces=[s.faces[0].id for s in inlets], quantity="Pressure")
            pout = app.post.evaluate_faces_quantity(faces=[s.faces[0].id for s in outlets], quantity="Pressure")
            dp = _stat(pin, "Mean", "mean") - _stat(pout, "Mean", "mean")
            q = a.vel * GAP * 1e-3 * H * 1e-3 * (N_DIE - 1)
            row.update(dp_Pa=dp, pumping_power_W=abs(dp) * q)
        its = [int(m.group(1)) for f in cdir.rglob("*.SOV") if (m := re.search(r"_(\d+)\.SOV$", f.name))]
        row["iterations"] = max(its) if its else ""
        for f in cdir.rglob("*.profile"):
            m = re.findall(r"Total Cells\\?', (\d+)", f.read_text(errors="ignore"))
            if m:
                row["cells"] = int(m[-1])
        row["status"] = "OK" if (row["iterations"] == "" or row["iterations"] < MAX_IT - 1) else "NOT_CONVERGED"
    except Exception as exc:
        row.update(status="FAILED", error=f"{type(exc).__name__}: {exc}")
        with (ROOT / "errors.log").open("a", encoding="utf-8") as fh:
            fh.write(f"\n===== {cdir.name} =====\n{traceback.format_exc()}")
    finally:
        if app is not None:
            try:
                app.save_project()
            except Exception:
                pass
            try:
                app.release_desktop(close_projects=True, close_desktop=True)
            except Exception:
                pass
    out = ROOT / "results_ndie.csv"
    new = not out.exists()
    with out.open("a", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            wr.writeheader()
        wr.writerow(row)
    print(f"Case status: {row['status']} cells={row['cells']} it={row['iterations']} {row['error']}", flush=True)


if __name__ == "__main__":
    main()
