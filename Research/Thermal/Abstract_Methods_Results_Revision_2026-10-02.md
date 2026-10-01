# V-Die inter-die cooling abstract — methods/results revision (2026-10-02)

Replaces the methods-to-conclusion part of the working abstract (from the pillar trade-off sentences through the final sentence). Responds to reviewer comment SK1: the study is **simulation-only**, so the text now states (1) the flow/heat-transfer physics and model assumptions, (2) the reduction relative to a top-side heat sink, and (3) how many dies a fixed stack height can hold before reaching a temperature limit. Process content (Cu electroplating, passivation) is omitted because no fabrication is claimed.

All numbers come from the Icepak study in [results summary](VDie_Icepak_Study_v3_Results_2026-10-02.md). Bracketed items are wording choices to confirm, not missing data.

## Revised text

In this work, we simulate single-phase water cooling through the gaps of a vertically oriented 40-die DRAM stack (11 mm × 11 mm × 200 µm dies, 175 µm gaps) and compare the inter-die passage with a top-side cold plate. Three-dimensional conjugate heat-transfer simulations (Ansys Icepak) solve steady, laminar flow of water with constant properties and a 25 °C inlet (Reynolds number below 1,200), coupled with conduction in the Si dies and Cu pillars. Each die carries a 3 W memory load, and the active die carries an additional 50 W/cm² I/O source over 0.3 mm × 0.3 mm. Pillar diameter (30–75 µm), pitch (150–300 µm), arrangement (in-line or staggered), and gap (125–250 µm) are varied, with pillar height equal to the gap, and configurations are compared at matched pumping power. Temperatures change by 1% or less under mesh refinement.

With an ideal top-side cold plate, heat must conduct along the 200-µm-thick die, and the peak die temperature rises by 50.4 K at 3 W per die, within 0.6% of the analytic solution. Inter-die flow at 0.5 m/s reduces the rise to 1.5 K with 0.08 W of pumping power for 39 gaps. Because the top-side rise scales inversely with die thickness, top-side cooling exceeds 85 °C beyond about 43 dies within the same 14.8 mm stack height, whereas inter-die flow removes heat through each die face.

At a matched stack pumping power of 1 W, staggered 75 µm pillars at 150 µm pitch reduce the hotspot temperature rise by 37% and the die-to-die temperature difference by 77% relative to a pillar-free gap; quadrupling the pumping power without pillars reduces the hotspot rise by only 17%. The pillars conduct heat into the adjacent die, raising its peak temperature by up to 0.1 K, and increase the pressure drop by 1.3–8 times at equal velocity. The diameter-to-pitch ratio sets most of the benefit (12–37% hotspot reduction), staggered arrays add 2–3 percentage points, and widening the gap from 125 to 250 µm increases the benefit of 75 µm pillars from 27% to 41%. The resulting design map defines pillar geometry for inter-die direct cooling and quantifies the thermal headroom for stacking additional DRAM dies within a fixed footprint.

## Changes vs. the commented draft
| Draft content | Revision | Reason |
|---|---|---|
| "we adjust the flow rate to compare… at matched pumping power" (method only) | Same method plus numbers (1 W stack pumping power) | Results now available |
| No physics description | Steady, laminar, incompressible, constant properties, conjugate, Re < 1,200, unit-cell symmetry, mesh/analytic checks | SK1: state how micro-channel physics is modeled |
| No baseline | Top-side ideal cold plate: 50.4 K vs 1.5 K | SK1: reduction vs top-side heat sink |
| "unlocks the thermal headroom required to stack more DRAM dies" (unsupported) | ~43-die limit for top-side at 85 °C (analytic, simulation-calibrated) | SK1: how many dies remain stable; claim now scoped |
| "coolant provides a thermal ground that reduces thermal crosstalk" (earlier paragraph) | **Fix needed in the earlier paragraph**: the pillar-free gap isolates adjacent dies best; pillars raise the neighbor-die temperature slightly while reducing ΔT_die-die | Data contradict "pillars reduce crosstalk" |
| "simultaneous scaling of both memory capacity and bandwidth" | Removed from results; keep only in the introduction if needed | Not evaluated by the simulation |

## Limits to keep in mind (do not overclaim)
- 3 W/die and the 0.3 mm I/O hotspot (+50 W/cm²) are assumed loads, not measured V-die power maps. Temperatures scale linearly with load (constant properties).
- The 43-die limit is an analytic extrapolation validated at N = 40 only; thinner dies were not simulated.
- Single-gap unit cell: manifold flow distribution across 39 gaps and interposer/underfill heat paths are excluded.
- Top-side baseline has zero TIM/cold-plate resistance (favorable to the baseline).
- Steady laminar model does not resolve unsteady pillar wakes.

## Optional novelty statement draft (48 words)
Single-phase water flow through the gaps of a vertically oriented 40-die DRAM stack reduces the peak die temperature rise from 50.4 K with a top-side cold plate to 1.5 K, and staggered Cu pillars reduce the I/O hotspot rise by a further 37% at matched pumping power.
