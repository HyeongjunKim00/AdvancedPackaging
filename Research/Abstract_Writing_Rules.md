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
