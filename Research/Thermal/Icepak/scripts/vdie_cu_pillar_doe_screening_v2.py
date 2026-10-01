"""Screening DOE for Cu-pillar-assisted inter-die liquid cooling in Icepak (v2).

v2 changes relative to vdie_cu_pillar_doe_screening.py
------------------------------------------------------
1. Root cause of the v1 failure: AEDT auto-created an *air* Region with 50 %
   padding around the model. The inlet/outlet/symmetry faces of the water box
   were therefore interior faces inside the air region, so AEDT reported
   "face does not have mesh" and stopped at "Populate Solver Input".
   v2 sets the Region padding to 0 in every direction, makes the Region itself
   the water domain, and deletes the separate water box.
2. Inlet/outlet openings are 2D sheets that cover only the gap cross-section
   on the Region's -Y/+Y faces. Transverse symmetry is assigned to the
   Region's +/-Z faces.
3. Unit cell = half die | gap | half die. A die inside a 40-die stack has a
   gap on both sides, so each die-half (100 um) carries half of one die's
   power. The die mid-planes (Region +/-X faces) are left as adiabatic walls,
   which is equivalent to symmetry there because those faces are solid.
   (v1 put two full dies with insulated backs on one gap, so each gap received
   2x the per-gap heat of an interior gap.)
   Set UNIT_CELL = "full_die_insulated" to reproduce the v1 heat assignment.
4. --single runs only the first case (empty channel, first velocity) to
   verify that one case solves before the DOE runs.
5. Energy-balance check: area-averaged outlet temperature rise x m_dot x cp
   versus the applied heat. An area average is not a mass-weighted bulk
   temperature, so a few-percent mismatch is expected for laminar flow.

This is a screening model. Mesh independence, contact, and full-stack
validation are required before treating results as final data.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import traceback
from datetime import datetime
from pathlib import Path

from ansys.aedt.core import Icepak


# -------------------------- User-editable inputs ----------------------------
AEDT_VERSION = None  # Example: "2026.1"; None selects the installed version.
RUN_ID = datetime.now().strftime("%Y%m%d_%H%M%S")
RUN_ROOT = Path(__file__).resolve().parent.parent / "Runs" / f"DOE_screening_v2_{RUN_ID}"
RESULTS_CSV = RUN_ROOT / "doe_results.csv"
MATCHED_PUMP_CSV = RUN_ROOT / "matched_pumping_power.csv"
ERROR_LOG = RUN_ROOT / "doe_errors.log"

# "half_die_symmetric": interior-die unit cell (recommended).
# "full_die_insulated": v1 heat assignment (two full dies, insulated backs).
UNIT_CELL = "half_die_symmetric"

# Representative channel geometry, mm. Flow is along +Y; the die gap is X.
DIE_THICKNESS_MM = 0.200
GAP_MM = 0.175
TRANSVERSE_WIDTH_MM = 1.200
PILLAR_ACTIVE_LENGTH_MM = 1.200
INLET_EXTENSION_MM = 0.600
OUTLET_EXTENSION_MM = 0.600

# Uniform heating scaled from the full die area.
FULL_DIE_WIDTH_MM = 11.0
FULL_DIE_HEIGHT_MM = 11.0
FULL_DIE_POWER_W = 3.0

# Water at approximately 25 C, single phase.
INLET_TEMPERATURE_C = 25.0
VELOCITIES_M_S = (0.5, 1.0, 2.0)
WATER_K_W_MK = 0.607
WATER_DENSITY_KG_M3 = 997.0
WATER_CP_J_KG_K = 4181.3
WATER_VISCOSITY_PA_S = 0.00089

DESIGNS = (
    {"name": "empty", "diameter_mm": 0.0, "pitch_mm": None},
    {"name": "cu_d50_p150", "diameter_mm": 0.050, "pitch_mm": 0.150},
    {"name": "cu_d50_p200", "diameter_mm": 0.050, "pitch_mm": 0.200},
)

GLOBAL_MESH_RESOLUTION = 4  # 1 (coarse) .. 5 (fine)
PILLAR_MESH_LEVEL = 5
# ----------------------------- End user inputs ------------------------------


def _float_result(value):
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, (list, tuple)):
        return _float_result(value[0])
    return float(str(value).split()[0])


def _stat(result, *keys):
    for key in keys:
        if key in result:
            return _float_result(result[key])
    raise RuntimeError(f"Expected one of {keys} in PyAEDT result: {result}")


def _faces_at(obj, axis_index, target_mm, tolerance_mm=1e-5):
    return [
        face.id
        for face in obj.faces
        if abs(float(face.center[axis_index]) - target_mm) <= tolerance_mm
    ]


def _segment_length_mm():
    return INLET_EXTENSION_MM + PILLAR_ACTIVE_LENGTH_MM + OUTLET_EXTENSION_MM


def _die_part_thickness_mm():
    if UNIT_CELL == "half_die_symmetric":
        return DIE_THICKNESS_MM / 2.0
    if UNIT_CELL == "full_die_insulated":
        return DIE_THICKNESS_MM
    raise ValueError(f"Unknown UNIT_CELL: {UNIT_CELL}")


def _die_part_power_w():
    """Power in each of the two die bodies of the segment."""
    segment_area_mm2 = TRANSVERSE_WIDTH_MM * _segment_length_mm()
    full_die_area_mm2 = FULL_DIE_WIDTH_MM * FULL_DIE_HEIGHT_MM
    one_die_segment_power = FULL_DIE_POWER_W * segment_area_mm2 / full_die_area_mm2
    if UNIT_CELL == "half_die_symmetric":
        return one_die_segment_power / 2.0
    return one_die_segment_power


def _build_geometry(app, design):
    length_mm = _segment_length_mm()
    t_die = _die_part_thickness_mm()

    die_a = app.modeler.create_box(
        origin=[-t_die, 0.0, 0.0],
        sizes=[t_die, length_mm, TRANSVERSE_WIDTH_MM],
        name="DRAM_Die_A",
        material="silicon",
    )
    die_b = app.modeler.create_box(
        origin=[GAP_MM, 0.0, 0.0],
        sizes=[t_die, length_mm, TRANSVERSE_WIDTH_MM],
        name="DRAM_Die_B",
        material="silicon",
    )

    pillars = []
    diameter_mm = design["diameter_mm"]
    pitch_mm = design["pitch_mm"]
    if diameter_mm > 0.0:
        if diameter_mm >= GAP_MM or diameter_mm >= pitch_mm:
            raise ValueError("Pillar diameter must be smaller than both gap and pitch.")
        rows = round(PILLAR_ACTIVE_LENGTH_MM / pitch_mm)
        cols = round(TRANSVERSE_WIDTH_MM / pitch_mm)
        if not math.isclose(rows * pitch_mm, PILLAR_ACTIVE_LENGTH_MM, abs_tol=1e-9):
            raise ValueError("Pillar active length must be an integer multiple of pitch.")
        if not math.isclose(cols * pitch_mm, TRANSVERSE_WIDTH_MM, abs_tol=1e-9):
            raise ValueError("Channel width must be an integer multiple of pitch.")

        for row, col in itertools.product(range(rows), range(cols)):
            y_center = INLET_EXTENSION_MM + (row + 0.5) * pitch_mm
            z_center = (col + 0.5) * pitch_mm
            pillar = app.modeler.create_cylinder(
                orientation="X",
                origin=[0.0, y_center, z_center],
                radius=diameter_mm / 2.0,
                height=GAP_MM,
                name=f"CuPillar_R{row + 1:02d}_C{col + 1:02d}",
                material="copper",
            )
            if not pillar:
                raise RuntimeError(f"Could not create pillar {row}, {col}.")
            pillars.append(pillar)

    # Region = model bounding box, filled with water (the coolant domain).
    # change_region_padding applies list element i to direction i, so all six
    # values must be given explicitly (a scalar only changes +X).
    if not app.modeler.change_region_padding(
        ["0"] * 6,
        padding_type=["Percentage Offset"] * 6,
        direction=["+X", "-X", "+Y", "-Y", "+Z", "-Z"],
    ):
        raise RuntimeError("Could not set Region padding to 0.")
    region = app.modeler["Region"]
    bb = region.bounding_box
    expected = [-t_die, 0.0, 0.0, GAP_MM + t_die, length_mm, TRANSVERSE_WIDTH_MM]
    if not all(math.isclose(float(a), b, abs_tol=1e-6) for a, b in zip(bb, expected)):
        raise RuntimeError(f"Region bounding box {bb} != expected {expected}.")
    region.material_name = "Water"
    if region.material_name.lower() != "water":
        raise RuntimeError(f"Region material is {region.material_name}, expected Water.")

    # Inlet/outlet sheets covering only the gap cross-section (XZ plane).
    inlet = _xz_sheet(app, 0.0, "Coolant_Inlet_Sheet")
    outlet = _xz_sheet(app, length_mm, "Coolant_Outlet_Sheet")

    return region, die_a, die_b, pillars, inlet, outlet


def _xz_sheet(app, y_mm, name):
    """Rectangle in the plane y = y_mm spanning x in [0, GAP], z in [0, W]."""
    # AEDT's width/height order for a ZX-plane rectangle is checked from the
    # created vertices; if swapped, the sheet is rebuilt with swapped sizes.
    for sizes in ([TRANSVERSE_WIDTH_MM, GAP_MM], [GAP_MM, TRANSVERSE_WIDTH_MM]):
        sheet = app.modeler.create_rectangle(
            orientation="ZX",
            origin=[0.0, y_mm, 0.0],
            sizes=sizes,
            name=name,
        )
        if not sheet:
            raise RuntimeError(f"Could not create sheet {name}.")
        xs = [float(v.position[0]) for v in sheet.vertices]
        ys = [float(v.position[1]) for v in sheet.vertices]
        zs = [float(v.position[2]) for v in sheet.vertices]
        ok = (
            math.isclose(min(xs), 0.0, abs_tol=1e-6)
            and math.isclose(max(xs), GAP_MM, abs_tol=1e-6)
            and math.isclose(min(zs), 0.0, abs_tol=1e-6)
            and math.isclose(max(zs), TRANSVERSE_WIDTH_MM, abs_tol=1e-6)
            and math.isclose(min(ys), y_mm, abs_tol=1e-6)
            and math.isclose(max(ys), y_mm, abs_tol=1e-6)
        )
        if ok:
            return sheet
        print(
            f"Sheet {name} extents x={min(xs)}..{max(xs)}, z={min(zs)}..{max(zs)}; "
            "retrying with swapped sizes.", flush=True,
        )
        app.modeler.delete(sheet.name)
    raise RuntimeError(f"Could not create sheet {name} matching the gap cross-section.")


def _run_case(design, velocity_m_s, run_root):
    case_id = f"{design['name']}_g175_v{velocity_m_s:g}".replace(".", "p")
    case_dir = run_root / case_id
    case_dir.mkdir(parents=True, exist_ok=True)
    project_path = case_dir / f"{case_id}.aedt"
    app = None
    die_power = _die_part_power_w()
    total_power = 2.0 * die_power

    try:
        app = Icepak(
            project=str(project_path),
            design=f"Icepak_{case_id}",
            version=AEDT_VERSION,
            non_graphical=False,
            new_desktop=True,
        )
        app.modeler.model_units = "mm"

        silicon = app.materials["silicon"]
        silicon.thermal_conductivity = "148"
        silicon.mass_density = "2330"
        silicon.specific_heat = "700"
        silicon.update()

        water = app.materials["water"]
        water.thermal_conductivity = str(WATER_K_W_MK)
        water.mass_density = str(WATER_DENSITY_KG_M3)
        water.specific_heat = str(WATER_CP_J_KG_K)
        water.viscosity = str(WATER_VISCOSITY_PA_S)
        water.update()

        copper = app.materials["copper"]
        copper.thermal_conductivity = "398"
        copper.mass_density = "8960"
        copper.specific_heat = "385"
        copper.update()

        region, die_a, die_b, pillars, inlet, outlet = _build_geometry(app, design)

        app.assign_solid_block(
            object_name=die_a.name,
            boundary_name="Die_A_Heat",
            power_assignment=f"{die_power:.12g}W",
        )
        app.assign_solid_block(
            object_name=die_b.name,
            boundary_name="Die_B_Heat",
            power_assignment=f"{die_power:.12g}W",
        )

        app.assign_velocity_free_opening(
            inlet.name,
            boundary_name="Coolant_Inlet",
            temperature=f"{INLET_TEMPERATURE_C}cel",
            velocity=["0m_per_sec", f"{velocity_m_s}m_per_sec", "0m_per_sec"],
        )
        app.assign_pressure_free_opening(
            outlet.name,
            boundary_name="Coolant_Outlet",
            temperature=f"{INLET_TEMPERATURE_C}cel",
            pressure=0.0,
        )

        symmetry_faces = sorted(
            set(_faces_at(region, 2, 0.0) + _faces_at(region, 2, TRANSVERSE_WIDTH_MM))
        )
        if len(symmetry_faces) != 2:
            raise RuntimeError(f"Expected 2 Region Z faces, found {symmetry_faces}.")
        app.assign_symmetry_wall(symmetry_faces, boundary_name="Transverse_Symmetry")

        global_mesh = app.mesh.global_mesh_region
        global_mesh.settings["MeshRegionResolution"] = GLOBAL_MESH_RESOLUTION
        global_mesh.update()
        if pillars:
            app.mesh.assign_mesh_region(
                assignment=[pillar.name for pillar in pillars],
                level=PILLAR_MESH_LEVEL,
                name="Fine_Pillars",
            )

        setup = app.create_setup(name="SteadyState", setup_type="IcepakSteadyState")
        setup.props["Flow Regime"] = "Laminar"
        setup.update()
        app.save_project()

        validation = app.validate_simple(log_file=str(case_dir / "validation.log"))
        print(f"Validation: {validation}", flush=True)

        status = app.analyze(setup=setup.name)
        if status is False:
            raise RuntimeError(
                "Icepak analyze returned False. Open the project and read Message Manager."
            )

        result_a = app.post.evaluate_object_quantity(
            object_name=die_a.name, quantity_name="Temperature", volume=True
        )
        result_b = app.post.evaluate_object_quantity(
            object_name=die_b.name, quantity_name="Temperature", volume=True
        )
        tmax_c = max(
            _stat(result_a, "Max", "max", "Maximum"),
            _stat(result_b, "Max", "max", "Maximum"),
        )
        tavg_c = (
            _stat(result_a, "Mean", "mean", "Average")
            + _stat(result_b, "Mean", "mean", "Average")
        ) / 2.0

        inlet_face = inlet.faces[0].id
        outlet_face = outlet.faces[0].id
        p_in = app.post.evaluate_faces_quantity(faces=[inlet_face], quantity="Pressure")
        p_out = app.post.evaluate_faces_quantity(faces=[outlet_face], quantity="Pressure")
        t_out = app.post.evaluate_faces_quantity(faces=[outlet_face], quantity="Temperature")
        delta_p_signed_pa = (
            _stat(p_in, "Mean", "mean", "Average") - _stat(p_out, "Mean", "mean", "Average")
        )
        delta_p_pa = abs(delta_p_signed_pa)
        flow_area_m2 = GAP_MM * 1e-3 * TRANSVERSE_WIDTH_MM * 1e-3
        flow_rate_m3_s = velocity_m_s * flow_area_m2
        pump_power_w = delta_p_pa * flow_rate_m3_s
        t_out_avg = _stat(t_out, "Mean", "mean", "Average")
        q_fluid_w = (
            WATER_DENSITY_KG_M3 * flow_rate_m3_s * WATER_CP_J_KG_K
            * (t_out_avg - INLET_TEMPERATURE_C)
        )

        return {
            "case_id": case_id,
            "status": "OK",
            "unit_cell": UNIT_CELL,
            "configuration": design["name"],
            "gap_um": GAP_MM * 1000.0,
            "pillar_diameter_um": design["diameter_mm"] * 1000.0,
            "pillar_pitch_um": design["pitch_mm"] * 1000.0 if design["pitch_mm"] else "",
            "inlet_velocity_m_s": velocity_m_s,
            "inlet_temperature_C": INLET_TEMPERATURE_C,
            "segment_total_power_W": total_power,
            "max_die_temperature_C": tmax_c,
            "average_die_temperature_C": tavg_c,
            "outlet_area_avg_temperature_C": t_out_avg,
            "energy_balance_ratio": q_fluid_w / total_power,
            "pressure_drop_Pa": delta_p_pa,
            "pressure_drop_signed_Pa": delta_p_signed_pa,
            "flow_rate_mL_min": flow_rate_m3_s * 60.0e6,
            "hydraulic_pumping_power_W": pump_power_w,
            "project_file": str(project_path),
            "error": "",
        }
    except Exception as exc:
        with (run_root / "doe_errors.log").open("a", encoding="utf-8") as log_file:
            log_file.write(f"\n===== {case_id} FAILED =====\n")
            log_file.write(f"{type(exc).__name__}: {exc}\n")
            log_file.write(traceback.format_exc())
        return {
            "case_id": case_id,
            "status": "FAILED",
            "unit_cell": UNIT_CELL,
            "configuration": design["name"],
            "gap_um": GAP_MM * 1000.0,
            "pillar_diameter_um": design["diameter_mm"] * 1000.0,
            "pillar_pitch_um": design["pitch_mm"] * 1000.0 if design["pitch_mm"] else "",
            "inlet_velocity_m_s": velocity_m_s,
            "inlet_temperature_C": INLET_TEMPERATURE_C,
            "segment_total_power_W": total_power,
            "max_die_temperature_C": "",
            "average_die_temperature_C": "",
            "outlet_area_avg_temperature_C": "",
            "energy_balance_ratio": "",
            "pressure_drop_Pa": "",
            "pressure_drop_signed_Pa": "",
            "flow_rate_mL_min": "",
            "hydraulic_pumping_power_W": "",
            "project_file": str(project_path),
            "error": f"{type(exc).__name__}: {exc}",
        }
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


def _write_matched_pump_table(rows, path, error_log):
    by_design = {}
    for row in rows:
        if row["status"] == "OK":
            by_design.setdefault(row["configuration"], []).append(row)
    if len(by_design) < 2:
        return

    ranges = []
    for design_rows in by_design.values():
        powers = [float(row["hydraulic_pumping_power_W"]) for row in design_rows]
        if len(powers) >= 2:
            ranges.append((min(powers), max(powers)))
    if len(ranges) < 2:
        return
    lower = max(item[0] for item in ranges)
    upper = min(item[1] for item in ranges)
    if upper <= lower:
        with error_log.open("a", encoding="utf-8") as file:
            file.write("No overlapping pumping-power interval; matched table skipped.\n")
        return

    targets = [lower + (upper - lower) * i / 4.0 for i in range(5)]
    out = []
    for design_name, design_rows in by_design.items():
        ordered = sorted(design_rows, key=lambda row: float(row["hydraulic_pumping_power_W"]))
        pvals = [float(row["hydraulic_pumping_power_W"]) for row in ordered]
        tvals = [float(row["max_die_temperature_C"]) for row in ordered]
        for target in targets:
            for idx in range(len(pvals) - 1):
                if pvals[idx] <= target <= pvals[idx + 1]:
                    if pvals[idx + 1] == pvals[idx]:
                        temp = 0.5 * (tvals[idx] + tvals[idx + 1])
                    else:
                        fraction = (target - pvals[idx]) / (pvals[idx + 1] - pvals[idx])
                        temp = tvals[idx] + fraction * (tvals[idx + 1] - tvals[idx])
                    out.append({
                        "configuration": design_name,
                        "matched_pumping_power_W": target,
                        "interpolated_max_die_temperature_C": temp,
                        "note": "Linear interpolation across three velocity samples; screening only.",
                    })
                    break
    if out:
        with path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=list(out[0].keys()))
            writer.writeheader()
            writer.writerows(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--single", action="store_true",
        help="Run only the empty channel at the first velocity (debug).",
    )
    args = parser.parse_args()

    RUN_ROOT.mkdir(parents=True, exist_ok=True)
    error_log = RUN_ROOT / "doe_errors.log"
    if error_log.exists():
        error_log.unlink()

    fields = [
        "case_id", "status", "unit_cell", "configuration", "gap_um",
        "pillar_diameter_um", "pillar_pitch_um", "inlet_velocity_m_s",
        "inlet_temperature_C", "segment_total_power_W", "max_die_temperature_C",
        "average_die_temperature_C", "outlet_area_avg_temperature_C",
        "energy_balance_ratio", "pressure_drop_Pa", "pressure_drop_signed_Pa",
        "flow_rate_mL_min", "hydraulic_pumping_power_W", "project_file", "error",
    ]
    cases = list(itertools.product(DESIGNS, VELOCITIES_M_S))
    if args.single:
        cases = cases[:1]

    rows = []
    consecutive_failures = 0
    for index, (design, velocity) in enumerate(cases, start=1):
        print(f"\n[{index}/{len(cases)}] {design['name']} at {velocity:g} m/s", flush=True)
        row = _run_case(design, velocity, RUN_ROOT)
        rows.append(row)
        with RESULTS_CSV.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Case status: {row['status']}  {row['error']}", flush=True)
        if row["status"] == "OK":
            consecutive_failures = 0
        else:
            consecutive_failures += 1
            if consecutive_failures >= 2:
                print("Stopping after two consecutive failed cases.", flush=True)
                break

    _write_matched_pump_table(rows, MATCHED_PUMP_CSV, error_log)
    failures = sum(row["status"] != "OK" for row in rows)
    print(f"\nAttempted {len(rows)} of {len(cases)} cases; failures: {failures}.", flush=True)
    print(f"Results CSV: {RESULTS_CSV}", flush=True)
    if error_log.exists():
        print(f"Error log: {error_log}", flush=True)


if __name__ == "__main__":
    main()
