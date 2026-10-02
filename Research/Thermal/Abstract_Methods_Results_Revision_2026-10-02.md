# V-Die inter-die cooling abstract — methods/results revision (2026-10-02)

Replaces the methods-to-conclusion part of the working abstract (from the pillar trade-off sentences through the final sentence). Responds to reviewer comment SK1: the study is **simulation-only**, so the text now states (1) the flow/heat-transfer physics and model assumptions, (2) the reduction relative to a top-side heat sink, and (3) how many dies a fixed stack height can hold before reaching a temperature limit. Process content (Cu electroplating, passivation) is omitted because no fabrication is claimed.

All numbers come from the Icepak study in [results summary](VDie_Icepak_Study_v3_Results_2026-10-02.md). Bracketed items are wording choices to confirm, not missing data.

## Revised text (v2, 2026-10-02 — unit cell + 10-die stack, 377 words)

We evaluate the scheme by three-dimensional conjugate heat-transfer simulation (Ansys Icepak), which solves steady, laminar flow of water with constant properties and a 25 °C inlet (channel Reynolds number below 1,200) coupled with conduction in the Si dies, Cu pillars, and Si interposer. Each die (11 mm × 11 mm × 200 µm) carries a 3 W memory load, and alternate dies carry an additional 50 W/cm² I/O source over 0.3 mm × 0.3 mm. A periodic inter-die unit cell resolves pillar diameter (30–75 µm), pitch (150–300 µm), arrangement (in-line or staggered), and gap (125–250 µm), with pillar height equal to the gap, and compares configurations at matched pumping power. A 10-die stack on the interposer then compares an isothermal top-side cold plate, with no coolant in the gaps, against inter-die flow with and without pillars. The pressure drop of the pillar-free gap agrees with the analytic laminar solution within 2%, and mesh refinement changes the peak temperature by less than 0.01 K.

With the top-side cold plate, heat conducts along the 11 mm die height through a 200 µm Si cross-section, and the peak die temperature rises by 51.4 K. Inter-die flow at 0.5 m/s reduces the rise to 3.0 K with 0.017 W of pumping power for the 10-die stack. Because the top-side temperature rise scales inversely with die thickness, an analytic conduction model calibrated by the simulation predicts that top-side cooling exceeds 85 °C beyond about 43 dies within a 14.8 mm stack height, whereas inter-die flow removes heat through each die face.

In the unit cell at matched pumping power, staggered 75 µm pillars at 150 µm pitch reduce the hotspot temperature rise by 37% and the die-to-die temperature difference by 77%, whereas quadrupling the pumping power without pillars reduces the hotspot rise by only 17%. In the 10-die stack, pillars placed only around the I/O sources lower the hotspot rise by 15–20% while increasing the pressure drop by 2.5% and raising the idle-die temperature by 0.16 K. The peak stack temperature occurs in the two end dies, which are cooled from one side only. The resulting design map defines pillar diameter, pitch, and placement for inter-die direct cooling and identifies end-die cooling as the next constraint on stacking additional DRAM dies within a fixed footprint.

> v1 (unit cell only) is superseded. v2 adds the 10-die stack (top-side cold plate without coolant vs inter-die flow with/without I/O-zone pillars) and drops "Temperatures change by 1%" in favor of the 10-die mesh check.

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
