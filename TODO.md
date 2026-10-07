# TODO

## P0 — V-Die study definition and ECTC abstract

- [ ] Reconcile the current study sequence: the latest discussion includes a 12-die HBM-representative benchmark and a 20-die pillar-layout sweep, while prior drafts proposed different die counts. Confirm one consistent simulation matrix before finalizing the abstract.
- [ ] Define the HBM reference and V-die conditions with matched per-die heat input, coolant, inlet temperature, and a clearly stated flow or pumping-power basis.
- [ ] Compare pillar-free, in-line, and staggered Cu-post configurations. The latest draft mentions 200 µm–1 mm pitch and 100 µm diameter/height, but confirm final geometry and which die count applies.
- [ ] Confirm the per-die power sweep and temperature limit. Prior drafts contain different power ranges; do not treat them as approved until confirmed.
- [ ] Evaluate Cu-to-Cu thermocompression bonding to a backside Cu landing pad, including bonding temperature, pressure, time, alignment, thermal budget, joint resistance, and bond strength.
- [ ] Select passivation material/thickness and coating sequence for coolant-facing die surfaces and exposed Cu-post sidewalls while keeping Cu-Cu bond interfaces clean.
- [ ] Use the two-die TTV to assess local structural/flow feasibility and validate local temperature and pressure-drop predictions. Do not claim full-stack validation from a two-die test vehicle.
- [ ] Update the abstract with measured/simulated results only after runs complete; preserve placeholders until then.
- [ ] Record the DLC setup operating range and the available TTV sensor/measurement plan.
- [ ] Verify that repository instructions are read by the AI tools in use (Codex, Claude, Gemini, Copilot).

## P1 — ECTC thermal-management background

- [ ] Review HBM cooling roadmap and relevant prior art.
- [ ] Summarize TIM bottlenecks and lid/spreader functions.
- [ ] Review direct liquid-cooling trends and single-phase baseline options.

## P2 — Product and market background

- [ ] Verify NVIDIA thermal-roadmap claims, including definitions and sources for power and cooling figures.

## Completed / superseded

- [x] Earlier 10–40-die scaling and full coolant × flow × pitch matrix superseded by the advisor-directed fixed 12-die sequence unless the study scope is revised again.
- [x] Previous 40-die PyAEDT debugging and earlier 10-die studies remain archived as historical work; they are not results for the revised 12-die study.

## Operations

- Keep evidence or output links with completed items.
- Save research findings in the relevant `Research/` files and update `AI_HANDOFF.md` at the end of each work session.
- Separate verified facts, source claims, assumptions, and inference.
