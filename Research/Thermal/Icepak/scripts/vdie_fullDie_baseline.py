"""Full-die (11 mm x 11 mm) comparison: top-side cold plate vs inter-die flow.

Unit cell: [half die A | gap | half die B], die mid-planes adiabatic
(= symmetry of an infinite stack of identical dies). Each die: uniform 3 W.
Axes: x = stacking axis, y = die width (flow direction for inter-die mode),
z = die height (z = 0: interposer edge, z = 11 mm: top edge).

--mode topside : no coolant in the gap (stagnant air, flow disabled).
                 Top edge (z = 11 mm) held at T_cold by an ideal isothermal
                 cold plate (best case for the top-side baseline: no TIM or
                 plate resistance). All other faces adiabatic (interposer
                 side conservatively adiabatic).
--mode interdie: water flows through the gap along +y at --vel; die edges
                 and gap top/bottom are adiabatic no-slip walls (sealed);
                 no top cold plate. No pillars (empty channel).
Results are appended to Runs/study_v3/fulldie_results.csv.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
import traceback
from pathlib import Path

from ansys.aedt.core import Icepak

STUDY_ROOT = Path(__file__).resolve().parent.parent / "Runs" / "study_v3"
CSV_PATH = STUDY_ROOT / "fulldie_results.csv"
DIE_W_MM = 11.0
DIE_H_MM = 11.0
DIE_T_MM = 0.200
T_COLD_C = 25.0
WATER = dict(k=0.607, rho=997.0, cp=4181.3, mu=0.00089)
FIELDS = ["case_id", "status", "mode", "die_power_W", "gap_um", "velocity_m_s",
          "Tmax_die_C", "Tavg_die_C", "dp_Pa", "flow_rate_mL_min_per_gap",
          "pumping_power_W_per_gap", "iterations", "cells", "project_file", "error"]


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


def _sheet(app, y, gap, name):
    for sizes in ([DIE_H_MM, gap], [gap, DIE_H_MM]):
        s = app.modeler.create_rectangle(orientation="ZX", origin=[0.0, y, 0.0],
                                         sizes=sizes, name=name)
        xs = [float(v.position[0]) for v in s.vertices]
        zs = [float(v.position[2]) for v in s.vertices]
        if math.isclose(max(xs), gap, abs_tol=1e-6) and math.isclose(max(zs), DIE_H_MM, abs_tol=1e-6):
            return s
        app.modeler.delete(s.name)
    raise RuntimeError("sheet")


def _last_iteration(proj):
    its = [int(m.group(1)) for f in proj.parent.rglob("*.SOV")
           if (m := re.search(r"_(\d+)\.SOV$", f.name))]
    return max(its) if its else -1


def _cells(proj):
    for f in proj.parent.rglob("*.profile"):
        m = re.findall(r"Total Cells\\?', (\d+)", f.read_text(errors="ignore"))
        if m:
            return int(m[-1])
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["topside", "interdie"], required=True)
    ap.add_argument("--power", type=float, default=3.0)
    ap.add_argument("--gap_um", type=float, default=175.0)
    ap.add_argument("--vel", type=float, default=0.5)
    ap.add_argument("--mesh", type=int, default=3)
    ap.add_argument("--tag", default="r3")
    a = ap.parse_args()
    STUDY_ROOT.mkdir(parents=True, exist_ok=True)
    gap = a.gap_um / 1000
    cid = f"full_{a.mode}_P{a.power:g}_g{a.gap_um:g}" + (f"_v{a.vel:g}" if a.mode == "interdie" else "")
    cid = cid.replace(".", "p") + f"_m{a.mesh}" + (f"_{a.tag}" if a.tag else "")
    proj = STUDY_ROOT / cid / f"{cid}.aedt"
    proj.parent.mkdir(parents=True, exist_ok=True)
    row = {k: "" for k in FIELDS}
    row.update(case_id=cid, mode=a.mode, die_power_W=a.power, gap_um=a.gap_um,
               velocity_m_s=a.vel if a.mode == "interdie" else "", project_file=str(proj))
    app = None
    try:
        app = Icepak(project=str(proj), design=f"Icepak_{cid}", non_graphical=False, new_desktop=True)
        app.modeler.model_units = "mm"
        si = app.materials["silicon"]
        si.thermal_conductivity, si.mass_density, si.specific_heat = "148", "2330", "700"
        si.update()
        t = DIE_T_MM / 2
        da = app.modeler.create_box([-t, 0, 0], [t, DIE_W_MM, DIE_H_MM], "DRAM_Die_A", "silicon")
        db = app.modeler.create_box([gap, 0, 0], [t, DIE_W_MM, DIE_H_MM], "DRAM_Die_B", "silicon")
        for obj, nm in ((da, "DieA_P"), (db, "DieB_P")):
            app.assign_solid_block(object_name=obj.name, boundary_name=nm,
                                   power_assignment=f"{a.power / 2:.12g}W")
        app.modeler.change_region_padding(["0"] * 6, padding_type=["Percentage Offset"] * 6,
                                          direction=["+X", "-X", "+Y", "-Y", "+Z", "-Z"])
        region = app.modeler["Region"]
        bb = [float(v) for v in region.bounding_box]
        if not math.isclose(bb[5], DIE_H_MM, abs_tol=1e-6):
            raise RuntimeError(f"Region bbox {bb}")
        setup = app.create_setup(name="SteadyState", setup_type="IcepakSteadyState")
        setup.props["Convergence Criteria - Max Iterations"] = 400
        if a.mode == "topside":
            # Isothermal top edges. AEDT 2026.1 silently stored a "Temperature"
            # source as 0 W Total Power (r2 run), so each candidate is verified by
            # reading the saved .aedt back; the first one that sticks is kept.
            app.edit_design_settings(ambient_temperature=T_COLD_C, radiation_temperature=T_COLD_C)
            top = _faces_at(da, 2, DIE_H_MM) + _faces_at(db, 2, DIE_H_MM)
            if len(top) != 2:
                raise RuntimeError(f"die top faces {top}")
            chosen = None
            for label, make in (
                ("source_fixed_temperature", lambda: app.assign_source(
                    top, thermal_condition="Fixed Temperature",
                    assignment_value=f"{T_COLD_C}cel", boundary_name="ColdPlate_Top")),
                ("wall_temperature", lambda: app.assign_stationary_wall_with_temperature(
                    top, name="ColdPlate_Top", temperature=f"{T_COLD_C}cel")),
            ):
                try:
                    b = make()
                except Exception as exc:
                    print(f"{label}: {exc}", flush=True)
                    continue
                if not b:
                    continue
                app.save_project()
                txt = Path(str(proj)).read_text(errors="ignore")
                blk = txt[txt.find("$begin 'ColdPlate_Top'"):txt.find("$end 'ColdPlate_Top'")]
                print(f"{label} stored as:\n{blk}", flush=True)
                ok_src = "Thermal Condition'='Fixed Temperature" in blk or \
                         "Thermal Condition'='Temperature" in blk
                ok_wall = "BoundType='Stationary Wall'" in blk and "Temperature" in blk \
                          and "'External Condition'='Temperature'" in blk
                if ok_src or ok_wall:
                    chosen = label
                    break
                b.delete()
            if not chosen:
                raise RuntimeError("No isothermal top boundary was accepted by AEDT.")
            row["error"] = f"top BC: {chosen}"
            setup.props["Include Flow"] = False
        else:
            w = app.materials["water"]
            w.thermal_conductivity = str(WATER["k"]); w.mass_density = str(WATER["rho"])
            w.specific_heat = str(WATER["cp"]); w.viscosity = str(WATER["mu"]); w.update()
            region.material_name = "Water"
            inlet = _sheet(app, 0.0, gap, "Coolant_Inlet_Sheet")
            outlet = _sheet(app, DIE_W_MM, gap, "Coolant_Outlet_Sheet")
            app.assign_velocity_free_opening(inlet.name, boundary_name="Coolant_Inlet",
                                             temperature=f"{T_COLD_C}cel",
                                             velocity=["0m_per_sec", f"{a.vel}m_per_sec", "0m_per_sec"])
            app.assign_pressure_free_opening(outlet.name, boundary_name="Coolant_Outlet",
                                             temperature=f"{T_COLD_C}cel", pressure=0.0)
            setup.props["Flow Regime"] = "Laminar"
            setup.props["Discretization Scheme - Momentum"] = "Second"
        gm = app.mesh.global_mesh_region
        gm.settings["MeshRegionResolution"] = a.mesh
        gm.update()
        setup.update()
        app.save_project()
        if app.analyze(setup=setup.name) is False:
            raise RuntimeError("analyze returned False")
        ra = app.post.evaluate_object_quantity(object_name=da.name, quantity_name="Temperature", volume=True)
        rb = app.post.evaluate_object_quantity(object_name=db.name, quantity_name="Temperature", volume=True)
        row.update(status="OK",
                   Tmax_die_C=max(_stat(ra, "Max", "max"), _stat(rb, "Max", "max")),
                   Tavg_die_C=0.5 * (_stat(ra, "Mean", "mean") + _stat(rb, "Mean", "mean")),
                   iterations=_last_iteration(proj), cells=_cells(proj))
        if a.mode == "interdie":
            pin = app.post.evaluate_faces_quantity(faces=[inlet.faces[0].id], quantity="Pressure")
            pout = app.post.evaluate_faces_quantity(faces=[outlet.faces[0].id], quantity="Pressure")
            dp = _stat(pin, "Mean", "mean") - _stat(pout, "Mean", "mean")
            q = a.vel * gap * 1e-3 * DIE_H_MM * 1e-3
            row.update(dp_Pa=dp, flow_rate_mL_min_per_gap=q * 6e7, pumping_power_W_per_gap=abs(dp) * q)
    except Exception as exc:
        row.update(status="FAILED", error=f"{type(exc).__name__}: {exc}")
        with (STUDY_ROOT / "errors.log").open("a", encoding="utf-8") as fh:
            fh.write(f"\n===== {cid} =====\n{traceback.format_exc()}")
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
    new = not CSV_PATH.exists()
    with CSV_PATH.open("a", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            wr.writeheader()
        wr.writerow(row)
    print(f"Case status: {row['status']} {row['error']}", flush=True)


if __name__ == "__main__":
    main()
