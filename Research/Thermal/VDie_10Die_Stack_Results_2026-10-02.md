# 10-die V-die stack — top-side cold plate vs inter-die water (with/without Cu pillars)

Ansys Icepak 2026.1 via PyAEDT, script `Icepak/scripts/vdie_ndie.py`. 40-die model was reduced to 10 dies (user decision, 2026-10-02) after mesh/AEDT stability problems at 40 dies.

## Model
- 10 Si dies, 11 (flow) × 11 (height) × 0.200 mm; 9 gaps of 0.175 mm; Si interposer 0.775 mm under the stack, truncated to the stack footprint (lateral spreading neglected); interposer bottom and stack outer faces adiabatic.
- Load: 3 W/die uniform; even dies (0, 2, 4, 6, 8) carry an extra I/O hotspot at the bottom edge, +50 W/cm² over 0.3 × 0.3 mm (assumed, not a measured power map). Total 30.2 W.
- **Top-side**: no coolant in gaps (stagnant air, flow off); die top edges fixed at 25 °C (ideal cold plate, zero TIM resistance).
- **Inter-die**: water, uniform 0.5 m/s at every gap inlet (ideal manifold), 25 °C, pressure outlet; steady laminar, constant properties; gap tops/bottoms sealed.
- **Cu pillar**: d 75 µm / p 150 µm staggered, only in a 1.2 × 1.2 mm patch around each I/O hotspot (60 pillars per gap, 540 total). Full-face pillars (~5,300 per gap) are not tractable in AEDT.

## Mesh notes (important for reuse)
- Icepak multi-level meshing (MLM) coarsened the gaps to ~3 cells and under-predicted Δp by ~3× regardless of max-size / min-elements-in-gap settings. **Disable MLM** (`EnableMLM=False`) in the global manual mesh: x 25 µm (7 cells across the gap), y/z 0.25 mm.
- Pillar case: solver crashed ("execution error on server") with max size ratio 5 → fixed with `MaxSizeRatio=2` and a manual 25 µm local region over hotspots + extreme pillars. A large object list in one mesh region or a model box as a refinement region also fails (AEDT drop / intersect error).
- Checks: empty-channel Δp 1,952 Pa vs analytic fully developed 1,918 Pa (+entrance effect); refinement 332k → 489k cells changes Tmax by 0.007 K and Δp by 3.4%; two different mesh strategies agree within 1.3% in Δp.

## Results (final runs with identical mesh settings for empty vs pillar)
| | Top-side cold plate | Inter-die, no pillar | Inter-die, Cu pillar |
|---|---|---|---|
| Stack Tmax rise (K) | **51.4** | 3.0 (end dies) | 3.0 (end dies) |
| Interior I/O hotspot rise (K) | 51.4 | 1.84–1.89 | **1.55–1.62** (−15 to −16%) |
| End-die I/O hotspot rise (K) | 51.4 | 2.25 | **1.80** (−20%) |
| Interior idle-die Tmax rise (K) | 51.0 | 1.71–1.80 | 1.87–1.96 (+0.16) |
| Δp (Pa) | — | 1,949 | 1,998 (+2.5%) |
| Pumping power, 9 gaps (W) | — | 0.0169 | 0.0173 |
| Cells / iterations | 334k / 75 | 321k / 96 | 838k / 157 |

## Interpretation
- Top-side cooling is limited by conduction along the 200 µm die height: 51.4 K vs 3.0 K for inter-die flow (consistent with the unit-cell result, 50.4 K vs 1.5 K; the 10-die value includes end dies and the bottom-edge hotspot).
- Hotspot-zone pillars lower the I/O hotspot by 15–16% (interior) and 20% (end die) for +2.5% Δp, while the neighboring idle dies warm by 0.16 K (heat redistribution through the pillars, same trend as the segment study).
- **New finding:** stack Tmax is set by the two end dies (cooled on one side only, outer face adiabatic), ~1.1 K above interior dies; pillars do not change it. Outer-face cooling (an extra coolant passage or cold wall beside the end dies) would be needed to bring end dies to the interior level — not simulated.

## Limits
- Assumed loads; ideal uniform manifold; interposer truncated; adiabatic outer faces (worst case for end dies); steady laminar.
- Pillars only in the I/O zone; full-face pillar effect is from the segment study (`VDie_Icepak_Study_v3_Results_2026-10-02.md`).
- Figure: `Icepak/results/n10/fig5_10die_comparison.png`.
