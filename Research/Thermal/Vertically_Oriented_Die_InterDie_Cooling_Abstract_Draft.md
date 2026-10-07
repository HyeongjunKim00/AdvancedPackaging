# V-Die Inter-Die Cooling Abstract

**Status:** Working draft updated after process discussion (2026-10-07). Cu posts have a dual mechanical-support and thermal-bridge role. The study matrix still needs reconciliation because current drafts mention different die counts and power/pitch ranges. Bracketed items require confirmation or results.

## Abstract

Realized compute throughput in artificial intelligence (AI) accelerators depends on memory capacity for resident model parameters and bandwidth for delivering weights and activations. High-bandwidth memory (HBM) expands capacity through horizontal DRAM stacking and supports high data rates through wide I/O interfaces. However, heat from lower DRAM dies must conduct through overlying dies and bonding interfaces before reaching the package cooling surface, adding thermal resistance as the stack grows. Vertically oriented DRAM architectures (V-die) have emerged to increase memory capacity and side-edge I/O density within a planar footprint comparable to an HBM stack [1], [2]. Vertical orientation replaces the through-stack heat path with in-plane conduction toward a top-mounted cold plate. However, each die must conduct heat along its height to a narrow upper edge, limiting the area available for top-side heat extraction as die power and stack density increase.

An inter-die liquid-cooling architecture is proposed to provide direct coolant access to the broad faces of vertically oriented DRAM dies. During wafer-level assembly, Cu pillars mechanically support neighboring dies and maintain gaps for coolant flow. The pillars are thermocompression-bonded to Cu landing pads on the backside of adjacent dies, providing a solid heat-conduction path between dies. The coolant-facing DRAM surfaces and exposed Cu-pillar sidewalls are conformally passivated to electrically isolate them from the coolant, while the Cu-to-Cu bond interfaces remain uncoated (**Figure 1(a)**). The bonded wafer stack is diced and mounted vertically on an interposer. This bonding and selective-passivation sequence is a proposed process route and remains to be validated for the target geometry.

To benchmark the cooling concept at an HBM4-representative die count and isolate the Cu-pillar contribution, simulations first evaluate a 12-die horizontal HBM reference with top-side cold-plate cooling and a 12-die V-die stack with inter-die liquid cooling. The V-die analysis examines a pillar-free gap and in-line and staggered Cu-pillar arrays with [fixed or swept pitch range], while keeping pillar diameter and height at [100 µm, if retained]. Maximum die temperature, die-level temperature distribution, and pressure drop quantify the thermal and hydraulic response under [specified per-die heat load], [coolant], [inlet temperature], and [flow condition].

After selecting a Cu-pillar configuration, the pillar geometry and cooling conditions are held fixed while per-die power is increased across [12, 16, 20, and 24 W per die, pending confirmation]. The resulting maximum-die-temperature versus power relationship identifies the per-die heat load that satisfies a specified temperature limit ([T_lim]). A two-die thermal test vehicle with passivated silicon dies and bonded Cu-pillar spacers assesses structural feasibility and validates local inter-die cooling predictions. Infrared thermography measures accessible die-surface temperatures, and inlet/outlet pressure measurements determine pressure drop under coolant flow.

The 12-die simulations quantify the change in maximum die temperature between the HBM reference and V-die configurations and isolate the contribution of each Cu-pillar arrangement. The power sweep identifies a maximum allowable load of [X W per die] under [T_lim] and [cooling conditions]. For the tested two-die configuration, measured surface temperatures and pressure drop agree with local simulations within [X% or X °C]. These results establish [quantified cooling benefit] and the thermal headroom supported by the proposed inter-die cooling architecture.

## Items to resolve before submission

- Confirm that 12, 16, 20, and 24 refer to W per die.
- Define the maximum allowable die temperature, coolant, inlet temperature, and flow or pumping condition.
- Select whether pillar pitch is fixed or swept during the initial 12-die pillar study. Confirm whether 100 µm diameter and height remain the selected values.
- Specify passivation material, thickness, and sequence. Keep Cu-Cu bonding interfaces uncoated and validate coating coverage on coolant-facing die surfaces and exposed pillar sidewalls.
- Confirm the Cu landing-pad design and thermocompression conditions. Literature reports process-specific examples near 180 °C and 400 °C; neither value is an established recipe for this target stack.
- Reconcile the die-count, per-die-power, and pitch ranges across the current abstract versions before selecting the final simulation matrix.
- Restrict two-die TTV validation claims to the tested local geometry. Do not describe a two-die TTV as full 12-die validation.
- Replace all result placeholders only with completed, traceable simulation or measurement data.
