# Abstract Writing Rules

## Purpose
Use these rules when drafting or revising research abstracts for the lab. Keep the prose concise, causal, technically specific, and consistent with the evidence available.

## Sentence logic
1. State the relevant technical need with a precise subject. Describe what system performance depends on; do not attribute intention or agency to a device.
   - Prefer: “AI-accelerator throughput depends on memory capacity and bandwidth.”
   - Avoid: “AI accelerators rely on advanced memory.”
2. Bring the problem definition forward. Use **However,** to pivot from the broad need to the unresolved physical or process constraint.
3. Introduce the present study early with **In this work,** and name the proposed structure or method.
4. Build the remaining sequence as: mechanism → method and comparison → quantitative result → scoped significance.
5. Make each sentence advance one part of the argument. Remove repeated background, claims, and conclusions.

## Subjects and physical mechanisms
- Make the actual component, process, or measured quantity the grammatical subject.
- State concrete cause and effect: structure or operating condition → heat-transfer/flow mechanism → measured temperature, resistance, pressure drop, or other outcome.
- Distinguish heat conduction through solids from convection into the coolant. Do not imply that a fin cools a die merely because it adds surface area.
- Identify coupled effects where relevant. For example, a pillar between two dies can add coolant-wetted area and conduct heat between the dies.
- Do not claim a structure solves a problem before the analysis or measurement supports that conclusion.

## Word choice and syntax
- Prefer **However,** to **but** for the key problem-definition pivot. Use the pivot deliberately; avoid repeating it without a new contrast.
- Use **In this work,** near the beginning to state the contribution.
- Minimize demonstrative pronouns such as **this** and **that** when their referents could be ambiguous. Repeat the specific noun when needed. “This” in the set phrase “In this work” is acceptable.
- Avoid vague or anthropomorphic statements such as “the accelerator relies on memory.” Name the dependency precisely, such as throughput, bandwidth, capacity, or power.
- Avoid unsupported evaluative terms including *excellent, superior, remarkable, significantly,* and unqualified *high/low*. Replace them with a value, comparison, or named physical condition.
- Replace broad terms such as *performance* with the relevant metric: maximum die temperature, thermal resistance, temperature nonuniformity, pressure drop, pumping power, or heat flux.
- Prefer specific active verbs such as *increases, reduces, conducts, transfers, convects, measures, compares,* and *simulates*. Avoid empty phrasing such as *was performed* or *it was shown*.

## Evidence and quantitative claims
- State test or simulation conditions alongside results: heat load or heat map, inlet temperature, flow rate, working fluid, and baseline as applicable.
- Report thermal and hydraulic measures together when the study concerns liquid cooling.
- Define comparison basis and reference case. Do not compare values taken under different conditions without explaining the difference.
- Keep unmeasured outcomes as explicit placeholders until validated. Never invent numerical results, model validation, reliability, or novelty claims.
- Mark assumptions and limitations. Do not imply mechanical-support validation when the study analyzes thermal behavior only.

## Titles
- Name the physical structure or mechanism and the study objective.
- Use “thermal–hydraulic” only when the study evaluates both heat transfer and fluid-flow quantities such as pressure drop or pumping power. Use “thermal” when the analysis addresses heat transfer alone.
- Avoid project nicknames when the title should describe the architecture to an external reader. Prefer descriptive wording such as “vertically oriented memory-die stacks.”


## Additional guidance from the V-Die abstract discussion
- Build the opening through a concrete technical chain before pivoting to the gap. For memory-integrated accelerators, distinguish **peak FLOPS** from **realized compute throughput**; explain the separate roles of resident parameter capacity and data-delivery bandwidth before introducing the package architecture.
- Make the transition from architecture to thermal problem explicit: state which surfaces the architecture creates, where coolant can reach, and what heat-transfer path is missing or uncertain.
- Do not force “However” into the first sentence. Establish enough technical context first, then use “However” for the specific limitation.
- Keep causal claims qualified when operating conditions matter. Prefer “can increase memory-side heat generation” to a universal claim unless workload power data support the stronger statement.
- Correct imprecise phrases such as “address these capacity and bandwidth.” Name the need: “address the need for greater memory capacity and I/O bandwidth.”
- A detailed opening is useful only when each detail advances the problem definition; avoid adding broad industry context that does not lead to the studied geometry, mechanism, or metric.

## Sentence focus and information order
- Put the central phenomenon or measured quantity near the beginning of the sentence when it is the main point of the study. In the current V-Die abstract, the first result concerns the thermal change as die count increases; lead with **thermal scaling / thermal response**, then state die count and the comparison between cooling architectures.
- Avoid automatically reframing a direct research statement as a subordinate clause beginning with **“how”** when that pushes the central subject later in the sentence. The reason is rhetorical: readers should encounter the study's main variable or outcome early, and the sentence should foreground the scientific question rather than its grammatical framing.
- Prefer concise, noun-led constructions such as: “Die-count-dependent thermal scaling is assessed by comparing top-side cold-plate cooling with inter-die liquid cooling.” A more explicit alternative is: “The thermal response is mapped across vertically oriented die stacks with increasing die counts under top-side cold-plate and inter-die liquid cooling.”
- Do not preserve a technically or grammatically awkward sentence merely to avoid “how.” Preserve the information priority—main phenomenon first—and rewrite the syntax naturally.
- For planned work before simulations or measurements, describe the comparison and metrics without result verbs or implied outcomes. Do not write that one architecture reduces temperature until validated data support the claim.
- When recording user feedback, preserve the rationale behind the edit (why the wording/order matters), not only a list of preferred or discouraged words.
- **Prefer metric-led sentences over author-led “We…” openings when natural.** Put the quantity being assessed (for example, maximum die temperature and coolant pressure drop) or the comparison itself in the grammatical subject position. The rationale is information order: readers should encounter the study's main evidence or question immediately, before the authors' action.
- Avoid replacing “We…” mechanically with passive voice. Use concise active constructions with a metric-led subject, such as: “Maximum die temperature and coolant pressure drop serve as the primary metrics for comparing pillar-free, in-line, and staggered inter-die cooling configurations across Cu-pillar pitches from 250 µm to 5 mm, with pillar diameter and height fixed at 100 µm.”


## Purpose-led study and result sequence
- State what scientific question each study step answers. A bare statement that cases “are compared” can sound exploratory or directionless; name the intended inference, such as isolating the Cu-pillar contribution, benchmarking an HBM4-representative stack, or determining thermal headroom under a specified temperature limit.
- For design studies, make the sequence explicit: establish a representative reference stack and baseline; vary one design feature to isolate its contribution under controlled conditions; fix the selected configuration and sweep the operating load to determine its thermal limit; then validate selected predictions experimentally.
- Keep geometry, heat load, coolant, flow condition, and comparison baseline explicit enough to support the intended inference. Avoid presenting an expansive parameter matrix without explaining what each sweep resolves.
- Write outcome sentences around the data needed to answer the stated question. For power-capability studies, relate per-die heat load to maximum die temperature and identify a maximum allowable load only after defining the temperature criterion.
- Scope validation claims to the test vehicle. A two-die TTV may validate local inter-die heat-transfer and pressure-drop predictions for the tested conditions; it does not by itself validate a 12-die stack trend or full-stack power limit.
- When advisor or reviewer feedback reveals a reusable reasoning rule, record both the rule and its rationale in this guide, then update `AI_HANDOFF.md` with the latest decision so future drafting does not repeat the same mistake.
- **Avoid the English word “set” in user-facing prose and abstract drafts.** The user has designated it as forbidden. Choose a verb that names the intended action: use “form” or “create” for a gap made by pillars, “define” when a dimension is specified, and “keep fixed” or “maintain constant” when a condition does not vary. Select the substitute by meaning, not by word replacement alone.


## Additional guidance — 2026-10-11: deliberate problem pivot and front-loaded sentences
- Reserve **“However,”** for the abstract's central, specific problem statement: a clearly established architecture or context followed by its unresolved limitation. Do not use it merely to connect two contrasting facts or to restate a drawback already explained. If the contrast is background rather than the core research gap, connect the ideas without “However,” or retain the user's original wording.
- Put the sentence's main point first. Lead with the key phenomenon, design trade-off, metric, result, or study purpose; do not make readers wait through a generic setup before reaching the claim.
- Prefer concise, direct, topic-led wording. A grammatical subject–verb sentence is acceptable, but it should foreground the scientific point rather than begin with author activity or a procedural preamble. Avoid passive or “noun-led” rewrites that obscure the causal relation.
- When revising, preserve the intended information hierarchy and the user's established abstract conventions. Do not mechanically compress by combining clauses if the result weakens the problem statement, causal logic, or emphasis.
- When identifying repetition, show the original wording and a proposed replacement side by side, then explain what information is retained, combined, or removed. Apply this format in discussions with the user as well as when proposing abstract edits.
- Rationale: the user reserves “However,” for the pivotal problem statement and prefers a top-first argument in which the central idea appears immediately. Generic contrast markers and delayed, author-led phrasing dilute that structure.
