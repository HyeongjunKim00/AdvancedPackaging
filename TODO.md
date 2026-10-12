# TODO

## P0 — V-Die study definition and ECTC abstract

- [ ] Revise the motivation paragraph to state that V-die was proposed to address HBM's TSV-based I/O routing-area constraint and stack thermal resistance. Explain capacity and bandwidth scaling through adding upright dies and side-edge I/O connections; explain the in-plane silicon heat path without claiming proven cooling improvement.
- [ ] Add a traceable source for the stated silicon thermal conductivity (*k* = 140 W/m·K) and confirm the applicable temperature/material condition.

- [ ] Define the direct comparison between two V-die cooling architectures: inter-die heat-path cooling with Cu heat-path layers and a top-mounted cold plate, and direct-to-silicon liquid cooling through gaps containing Cu pillars. HBM is background motivation, not the core cooling benchmark.
- [ ] Define matched geometry, die count, per-die heat input, boundary conditions, and temperature ceiling. For the liquid-cooling architecture, specify coolant, inlet temperature, flow or pumping-power basis.
- [ ] Design die-count and per-die-power sweeps to identify the maximum die count and thermal load each architecture supports below the DRAM temperature limit. Confirm the ranges before writing them into the abstract.
- [ ] Define the Cu heat-path layer geometry in the cold-plate reference and Cu-pillar geometry, pitch, and arrangement in direct liquid cooling. Confirm whether 100 µm diameter/height and prior pitch ranges remain applicable.
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
