# V-Die inter-die cooling abstract — methods/results revision (2026-10-02)

Replaces the methods-to-conclusion part of the working abstract (from the pillar trade-off sentences through the final sentence). Responds to reviewer comment SK1: the study is **simulation-only**, so the text now states (1) the flow/heat-transfer physics and model assumptions, (2) the reduction relative to a top-side heat sink, and (3) how many dies a fixed stack height can hold before reaching a temperature limit. Process content (Cu electroplating, passivation) is omitted because no fabrication is claimed.

All numbers come from the Icepak study in [results summary](VDie_Icepak_Study_v3_Results_2026-10-02.md). Bracketed items are wording choices to confirm, not missing data.

## Revised text v3 (2026-10-02, current) — physics-focused, no specific numbers, 325 words

사용자 요청: 수치를 빼고 "어떤 physics를 반영하는지" 중심으로. 수치는 결과 문서에 보관하고 필요 시 다시 넣는다.

We evaluate the scheme with three-dimensional conjugate heat-transfer simulations that couple heat conduction in the Si dies, Cu pillars, and Si interposer with convective heat transfer to the coolant. Because the inter-die gaps are only a few hundred micrometers wide, the coolant flow is treated as steady, incompressible, single-phase laminar flow, and the momentum and energy equations are solved together with conduction in the solids. Each die carries a uniform memory heat load, and selected dies carry an additional localized I/O heat source. Coolant enters every gap at a fixed velocity and temperature and leaves through a pressure outlet. A periodic inter-die unit cell is used to vary pillar diameter, pitch, arrangement (in-line or staggered), and inter-die spacing, with pillar height set by the gap, and the configurations are compared at matched pumping power. A multi-die stack on the interposer then compares inter-die cooling with and without pillars against a top-side cold plate, modeled as an isothermal boundary on the die top edges with no coolant in the gaps. The model is checked against the analytic laminar pressure drop of a parallel-plate channel and by mesh refinement.

With top-side cooling, heat must conduct along the full die height through the thin Si cross-section, so the peak die temperature increases as the dies become thinner, which limits the number of dies that fit within a fixed stack height. Inter-die flow removes heat through each die face and lowers the peak temperature by more than an order of magnitude at small pumping power. At matched pumping power, the pillars lower the I/O hotspot temperature and the die-to-die temperature difference more effectively than an increased flow rate, at the cost of a higher pressure drop and heat conduction into adjacent dies. In the stack, the end dies, cooled from one side only, set the peak temperature. The resulting design map relates pillar geometry and placement to hotspot temperature, die-to-die temperature uniformity, and pumping power for inter-die direct cooling.

### 반영한 physics (설명용)
- Conjugate heat transfer: 고체(Si die, Cu pillar, 인터포저) 전도 + 냉각수 대류를 한 모델에서 동시에 푼다.
- 유동: gap이 수백 µm라 Re가 작음 → 정상, 비압축, 단상, 층류. 운동량 + 에너지 방정식.
- 경계조건: 입구 속도·온도 고정, 출구 압력; top-side 기준은 die 상단 등온(이상적 cold plate), gap 유체 없음.
- 열원: die 균일 메모리 발열 + 일부 die의 국부 I/O 발열.
- 비교 기준: 동일 펌핑동력. 검증: 평행평판 층류 압력강하 해석해, 메쉬 세분화.

---

## Superseded: v2 (numbers included)

### v2 text (, 2026-10-02 — unit cell + 10-die stack, 377 words)

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
