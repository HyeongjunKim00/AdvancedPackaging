"""V-die inter-die cooling study v3 (one design, several velocities per call).

Unit cell (x = die-stacking axis, y = flow, z = transverse):
    [half die A | gap (water, Cu pillars) | half die B]
Die mid-planes (Region +/-X) are adiabatic = symmetry for an alternating
stack ... A | gap | B | gap | A ...  Z faces are symmetry planes.

Loads (per full die, scaled to the 2.4 mm x 1.2 mm segment area):
  * Both dies: baseline memory load 3 W / (11 mm x 11 mm) = 2.48 W/cm^2.
  * Die A only: localized I/O hotspot, extra HOTSPOT_FLUX_W_CM2 over a
    0.3 mm x 0.3 mm patch at the centre of the pillar array.
    -> die A = "active" die with I/O hotspot, die B = neighbouring die.
These loads are modelling assumptions, not measured V-die power maps.

Physics: steady, laminar, single-phase water with constant properties,
conjugate conduction in Si and Cu. Re_Dh < ~800 for all cases (laminar).

Outputs are appended to Runs/study_v3/results.csv; a case already marked OK
is skipped, so the script can be re-queued safely.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import re
import traceback
from pathlib import Path

from ansys.aedt.core import Icepak

STUDY_ROOT = Path(__file__).resolve().parent.parent / "Runs" / "study_v3"
RESULTS_CSV = STUDY_ROOT / "results.csv"

DIE_THICKNESS_MM = 0.200
TRANSVERSE_WIDTH_MM = 1.200
PILLAR_ACTIVE_LENGTH_MM = 1.200
INLET_EXTENSION_MM = 0.600
OUTLET_EXTENSION_MM = 0.600

FULL_DIE_AREA_MM2 = 11.0 * 11.0
FULL_DIE_POWER_W = 3.0
HOTSPOT_SIZE_MM = 0.300
HOTSPOT_FLUX_W_CM2 = 50.0  # extra flux on die A patch (assumption)

INLET_TEMPERATURE_C = 25.0
WATER = dict(k=0.607, rho=997.0, cp=4181.3, mu=0.00089)
MAX_ITERATIONS = 400

FIELDS = [
    "case_id", "status", "design", "arrangement", "gap_um", "pillar_diameter_um",
    "pillar_pitch_um", "n_pillars", "velocity_m_s", "Re_Dh", "mesh_resolution",
    "hotspot_flux_W_cm2", "segment_power_W",
    "T_hotspot_C", "Tmax_dieA_C", "Tavg_dieA_C", "Tmax_dieB_C", "Tavg_dieB_C",
    "dT_die_die_max_C", "dT_die_die_avg_C",
    "dp_Pa", "flow_rate_mL_min", "pumping_power_W",
    "iterations", "converged", "cells", "project_file", "error",
]


def _num(value):
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, (list, tuple)):
        return _num(value[0])
    return float(str(value).split()[0])


def _stat(result, *keys):
    for key in keys:
        if key in result:
            return _num(result[key])
    raise RuntimeError(f"Expected one of {keys} in {result}")


def _faces_at(obj, axis, target, tol=1e-5):
    return [f.id for f in obj.faces if abs(float(f.center[axis]) - target) <= tol]


def _length():
    return INLET_EXTENSION_MM + PILLAR_ACTIVE_LENGTH_MM + OUTLET_EXTENSION_MM


def _sheet(app, y_mm, gap_mm, name):
    for sizes in ([TRANSVERSE_WIDTH_MM, gap_mm], [gap_mm, TRANSVERSE_WIDTH_MM]):
        sheet = app.modeler.create_rectangle(
            orientation="ZX", origin=[0.0, y_mm, 0.0], sizes=sizes, name=name
        )
        xs = [float(v.position[0]) for v in sheet.vertices]
        zs = [float(v.position[2]) for v in sheet.vertices]
        if (math.isclose(max(xs), gap_mm, abs_tol=1e-6) and math.isclose(min(xs), 0, abs_tol=1e-6)
                and math.isclose(max(zs), TRANSVERSE_WIDTH_MM, abs_tol=1e-6)):
            return sheet
        app.modeler.delete(sheet.name)
    raise RuntimeError(f"Could not create sheet {name}")


def _pillar_centres(pitch, arrangement):
    rows = round(PILLAR_ACTIVE_LENGTH_MM / pitch)
    cols = round(TRANSVERSE_WIDTH_MM / pitch)
    if not (math.isclose(rows * pitch, PILLAR_ACTIVE_LENGTH_MM, abs_tol=1e-9)
            and math.isclose(cols * pitch, TRANSVERSE_WIDTH_MM, abs_tol=1e-9)):
        raise ValueError("Array length/width must be integer multiples of pitch.")
    centres = []
    for r in range(rows):
        y = INLET_EXTENSION_MM + (r + 0.5) * pitch
        if arrangement == "staggered" and r % 2 == 1:
            zs = [c * pitch for c in range(cols + 1)]  # edge pillars cut in half
        else:
            zs = [(c + 0.5) * pitch for c in range(cols)]
        centres += [(y, z) for z in zs]
    return centres


def _build(app, gap, d, pitch, arrangement):
    L = _length()
    t = DIE_THICKNESS_MM / 2.0
    die_a = app.modeler.create_box([-t, 0, 0], [t, L, TRANSVERSE_WIDTH_MM], "DRAM_Die_A", "silicon")
    die_b = app.modeler.create_box([gap, 0, 0], [t, L, TRANSVERSE_WIDTH_MM], "DRAM_Die_B", "silicon")
    y0 = INLET_EXTENSION_MM + PILLAR_ACTIVE_LENGTH_MM / 2 - HOTSPOT_SIZE_MM / 2
    z0 = TRANSVERSE_WIDTH_MM / 2 - HOTSPOT_SIZE_MM / 2
    hot = app.modeler.create_box([-t, y0, z0], [t, HOTSPOT_SIZE_MM, HOTSPOT_SIZE_MM],
                                 "DieA_IO_Hotspot", "silicon")
    if not app.modeler.subtract(die_a, hot, keep_originals=True):
        raise RuntimeError("Hotspot subtraction failed")

    pillars = []
    if d > 0:
        if d >= gap or d >= pitch:
            raise ValueError("Pillar diameter must be smaller than gap and pitch.")
        for i, (y, z) in enumerate(_pillar_centres(pitch, arrangement)):
            p = app.modeler.create_cylinder("X", [0.0, y, z], d / 2.0, gap,
                                            name=f"CuPillar_{i:04d}", material="copper")
            if not p:
                raise RuntimeError(f"Pillar {i} creation failed")
            pillars.append(p)
        if arrangement == "staggered":
            cut_lo = app.modeler.create_box([-1, 0, -1], [3, L, 1], "cut_lo")
            cut_hi = app.modeler.create_box([-1, 0, TRANSVERSE_WIDTH_MM], [3, L, 1], "cut_hi")
            edge = [p for p in pillars
                    if abs(float(p.bounding_box[2]) + d / 2) < 1e-6
                    or abs(float(p.bounding_box[5]) - TRANSVERSE_WIDTH_MM - d / 2) < 1e-6]
            if edge:
                app.modeler.subtract(edge, [cut_lo, cut_hi], keep_originals=False)
            else:
                app.modeler.delete([cut_lo.name, cut_hi.name])

    app.modeler.change_region_padding(["0"] * 6, padding_type=["Percentage Offset"] * 6,
                                      direction=["+X", "-X", "+Y", "-Y", "+Z", "-Z"])
    region = app.modeler["Region"]
    bb = [float(v) for v in region.bounding_box]
    exp = [-t, 0, 0, gap + t, L, TRANSVERSE_WIDTH_MM]
    if not all(math.isclose(a, b, abs_tol=1e-6) for a, b in zip(bb, exp)):
        raise RuntimeError(f"Region bbox {bb} != {exp}")
    region.material_name = "Water"
    inlet = _sheet(app, 0.0, gap, "Coolant_Inlet_Sheet")
    outlet = _sheet(app, L, gap, "Coolant_Outlet_Sheet")
    return region, die_a, die_b, hot, pillars, inlet, outlet


def _last_iteration(project_path):
    its = []
    for f in project_path.parent.rglob("*.SOV"):
        m = re.search(r"_(\d+)\.SOV$", f.name)
        if m:
            its.append(int(m.group(1)))
    return max(its) if its else -1


def _cells(project_path):
    for f in project_path.parent.rglob("*.profile"):
        m = re.findall(r"Total Cells\\?', (\d+)", f.read_text(errors="ignore"))
        if m:
            return int(m[-1])
    return ""


def run_case(args, v):
    gap = args.gap_um / 1000.0
    d = args.d_um / 1000.0
    pitch = args.p_um / 1000.0 if args.p_um else None
    arr = args.arrangement if d > 0 else "none"
    tag = f"_{args.tag}" if args.tag else ""
    case_id = (f"{args.design}_g{args.gap_um:g}_v{v:g}_m{args.mesh}{tag}").replace(".", "p")
    case_dir = STUDY_ROOT / case_id
    n = 2
    while (case_dir / f"{case_dir.name}.aedt").exists():  # never reopen a stale project
        case_dir = STUDY_ROOT / f"{case_id}_r{n}"
        n += 1
    case_dir.mkdir(parents=True, exist_ok=True)
    proj = case_dir / f"{case_dir.name}.aedt"

    L = _length()
    seg_area = TRANSVERSE_WIDTH_MM * L
    p_die_seg = FULL_DIE_POWER_W * seg_area / FULL_DIE_AREA_MM2      # one die, segment
    f_hot = HOTSPOT_SIZE_MM ** 2 / seg_area
    q_hot_extra = HOTSPOT_FLUX_W_CM2 * 1e-2 * HOTSPOT_SIZE_MM ** 2   # W, full die thickness
    p_a_rem = 0.5 * p_die_seg * (1 - f_hot)
    p_hot = 0.5 * p_die_seg * f_hot + 0.5 * q_hot_extra
    p_b = 0.5 * p_die_seg
    seg_power = p_a_rem + p_hot + p_b
    dh = 2 * gap * 1e-3
    re_dh = WATER["rho"] * v * dh / WATER["mu"]

    row = {k: "" for k in FIELDS}
    row.update(case_id=case_id, design=args.design, arrangement=arr, gap_um=args.gap_um,
               pillar_diameter_um=args.d_um, pillar_pitch_um=args.p_um or "",
               velocity_m_s=v, Re_Dh=round(re_dh, 1), mesh_resolution=args.mesh,
               hotspot_flux_W_cm2=HOTSPOT_FLUX_W_CM2, segment_power_W=seg_power,
               project_file=str(proj))
    app = None
    try:
        app = Icepak(project=str(proj), design=f"Icepak_{case_id}", non_graphical=False,
                     new_desktop=True)
        app.modeler.model_units = "mm"
        for name, props in (("silicon", (148, 2330, 700)), ("copper", (398, 8960, 385))):
            m = app.materials[name]
            m.thermal_conductivity, m.mass_density, m.specific_heat = map(str, props)
            m.update()
        w = app.materials["water"]
        w.thermal_conductivity = str(WATER["k"]); w.mass_density = str(WATER["rho"])
        w.specific_heat = str(WATER["cp"]); w.viscosity = str(WATER["mu"]); w.update()

        region, die_a, die_b, hot, pillars, inlet, outlet = _build(app, gap, d, pitch, arr)
        row["n_pillars"] = len(pillars)
        for obj, pw, nm in ((die_a, p_a_rem, "DieA_Base"), (hot, p_hot, "DieA_IO"),
                            (die_b, p_b, "DieB_Base")):
            app.assign_solid_block(object_name=obj.name, boundary_name=nm,
                                   power_assignment=f"{pw:.12g}W")
        app.assign_velocity_free_opening(inlet.name, boundary_name="Coolant_Inlet",
                                         temperature=f"{INLET_TEMPERATURE_C}cel",
                                         velocity=["0m_per_sec", f"{v}m_per_sec", "0m_per_sec"])
        app.assign_pressure_free_opening(outlet.name, boundary_name="Coolant_Outlet",
                                         temperature=f"{INLET_TEMPERATURE_C}cel", pressure=0.0)
        sym = sorted(set(_faces_at(region, 2, 0.0) + _faces_at(region, 2, TRANSVERSE_WIDTH_MM)))
        if len(sym) != 2:
            raise RuntimeError(f"Region Z faces: {sym}")
        app.assign_symmetry_wall(sym, boundary_name="Transverse_Symmetry")

        gm = app.mesh.global_mesh_region
        gm.settings["MeshRegionResolution"] = args.mesh
        gm.update()
        fine = [hot.name] + [p.name for p in pillars]
        app.mesh.assign_mesh_region(assignment=fine, level=5, name="Fine_Local")

        setup = app.create_setup(name="SteadyState", setup_type="IcepakSteadyState")
        setup.props["Flow Regime"] = "Laminar"
        setup.props["Convergence Criteria - Max Iterations"] = MAX_ITERATIONS
        setup.props["Discretization Scheme - Momentum"] = "Second"
        setup.update()
        app.save_project()
        if app.analyze(setup=setup.name) is False:
            raise RuntimeError("analyze returned False")

        def tq(name):
            r = app.post.evaluate_object_quantity(object_name=name, quantity_name="Temperature",
                                                  volume=True)
            return _stat(r, "Max", "max", "Maximum"), _stat(r, "Mean", "mean", "Average")

        a_max, a_avg = tq(die_a.name)
        h_max, h_avg = tq(hot.name)
        b_max, b_avg = tq(die_b.name)
        vol_a = (DIE_THICKNESS_MM / 2) * (seg_area - HOTSPOT_SIZE_MM ** 2)
        vol_h = (DIE_THICKNESS_MM / 2) * HOTSPOT_SIZE_MM ** 2
        a_avg_all = (a_avg * vol_a + h_avg * vol_h) / (vol_a + vol_h)
        pin = app.post.evaluate_faces_quantity(faces=[inlet.faces[0].id], quantity="Pressure")
        pout = app.post.evaluate_faces_quantity(faces=[outlet.faces[0].id], quantity="Pressure")
        dp = _stat(pin, "Mean", "mean", "Average") - _stat(pout, "Mean", "mean", "Average")
        q = v * gap * 1e-3 * TRANSVERSE_WIDTH_MM * 1e-3
        it = _last_iteration(proj)
        row.update(status="OK", T_hotspot_C=h_max, Tmax_dieA_C=max(a_max, h_max),
                   Tavg_dieA_C=a_avg_all, Tmax_dieB_C=b_max, Tavg_dieB_C=b_avg,
                   dT_die_die_max_C=max(a_max, h_max) - b_max,
                   dT_die_die_avg_C=a_avg_all - b_avg, dp_Pa=dp,
                   flow_rate_mL_min=q * 6e7, pumping_power_W=abs(dp) * q,
                   iterations=it, converged=(0 <= it < MAX_ITERATIONS - 1), cells=_cells(proj))
    except Exception as exc:
        row.update(status="FAILED", error=f"{type(exc).__name__}: {exc}")
        with (STUDY_ROOT / "errors.log").open("a", encoding="utf-8") as fh:
            fh.write(f"\n===== {case_id} =====\n{traceback.format_exc()}")
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
    if row["status"] == "OK" and not row["converged"]:
        row["status"] = "NOT_CONVERGED"
    return row


def _done_ids():
    if not RESULTS_CSV.exists():
        return set()
    with RESULTS_CSV.open(encoding="utf-8") as fh:
        return {r["case_id"] for r in csv.DictReader(fh) if r["status"] == "OK"}


def _append(row):
    new = not RESULTS_CSV.exists()
    with RESULTS_CSV.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--design", required=True)
    ap.add_argument("--d_um", type=float, default=0.0)
    ap.add_argument("--p_um", type=float, default=0.0)
    ap.add_argument("--arrangement", default="inline", choices=["inline", "staggered"])
    ap.add_argument("--gap_um", type=float, default=175.0)
    ap.add_argument("--vel", type=float, nargs="+", default=[0.5, 1.0, 2.0])
    ap.add_argument("--mesh", type=int, default=4)
    ap.add_argument("--tag", default="")
    args = ap.parse_args()
    STUDY_ROOT.mkdir(parents=True, exist_ok=True)
    done = _done_ids()
    for v in args.vel:
        cid = (f"{args.design}_g{args.gap_um:g}_v{v:g}_m{args.mesh}"
               + (f"_{args.tag}" if args.tag else "")).replace(".", "p")
        if cid in done:
            print(f"skip {cid} (already OK)", flush=True)
            continue
        print(f"\n=== {cid} ===", flush=True)
        row = run_case(args, v)
        _append(row)
        print(f"Case status: {row['status']} it={row['iterations']} {row['error']}", flush=True)


if __name__ == "__main__":
    main()
