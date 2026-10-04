# V-Die Inter-Die Cooling Abstract

**Status:** Revised working draft following advisor feedback (2026-10-04). The study sequence is updated to a fixed 12-die benchmark, Cu-pillar assessment, per-die power sweep, and TTV validation. Bracketed items require confirmation or results.

## Abstract

Realized compute throughput in artificial intelligence (AI) accelerators depends on memory capacity for resident model parameters and bandwidth for delivering weights and activations. High-bandwidth memory (HBM) expands capacity through horizontal DRAM stacking and supports high data rates through wide I/O interfaces. However, heat from lower DRAM dies must conduct through overlying dies and bonding interfaces before reaching the package cooling surface, adding thermal resistance as the stack grows. Vertically oriented DRAM architectures (V-die) have emerged to increase memory capacity and side-edge I/O density within a planar footprint comparable to an HBM stack [1], [2]. Vertical orientation replaces the through-stack heat path with in-plane conduction toward a top-mounted cold plate. However, each die must conduct heat along its height to a narrow upper edge, limiting the area available for top-side heat extraction as die power and stack density increase.

An inter-die liquid-cooling architecture is proposed to provide direct coolant access to the broad faces of vertically oriented DRAM dies. During wafer-level assembly, Cu pillars are formed on passivated DRAM wafers and bonded to the backside of neighboring wafers. The bonded pillars support the dies and maintain inter-die gaps that serve as coolant passages. The passivation layer separates the DRAM surfaces from the coolant, while exposed Cu-pillar surfaces add coolant-contact area (**Figure 1(a)**). The bonded wafer stack is diced and mounted vertically on an interposer.

To benchmark the cooling concept at an HBM4-representative die count and isolate the Cu-pillar contribution, simulations first evaluate a 12-die horizontal HBM reference with top-side cold-plate cooling and a 12-die V-die stack with inter-die liquid cooling. The V-die analysis examines a pillar-free gap and in-line and staggered Cu-pillar arrays with [fixed or swept pitch range], while keeping pillar diameter and height at [100 µm, if retained]. Maximum die temperature, die-level temperature distribution, and pressure drop quantify the thermal and hydraulic response under [specified per-die heat load], [coolant], [inlet temperature], and [flow condition].

After selecting a Cu-pillar configuration, the pillar geometry and cooling conditions are held fixed while per-die power is increased across [12, 16, 20, and 24 W per die, pending confirmation]. The resulting maximum-die-temperature versus power relationship identifies the per-die heat load that satisfies a specified temperature limit ([T_lim]). A two-die thermal test vehicle with passivated silicon dies and bonded Cu-pillar spacers assesses structural feasibility and validates local inter-die cooling predictions. Infrared thermography measures accessible die-surface temperatures, and inlet/outlet pressure measurements determine pressure drop under coolant flow.

The 12-die simulations quantify the change in maximum die temperature between the HBM reference and V-die configurations and isolate the contribution of each Cu-pillar arrangement. The power sweep identifies a maximum allowable load of [X W per die] under [T_lim] and [cooling conditions]. For the tested two-die configuration, measured surface temperatures and pressure drop agree with local simulations within [X% or X °C]. These results establish [quantified cooling benefit] and the thermal headroom supported by the proposed inter-die cooling architecture.

## Items to resolve before submission

- Confirm that 12, 16, 20, and 24 refer to W per die.
- Define the maximum allowable die temperature, coolant, inlet temperature, and flow or pumping condition.
- Select whether pillar pitch is fixed or swept during the initial 12-die pillar study. Confirm whether 100 µm diameter and height remain the selected values.
- Specify passivation material and thickness. Keep the selected coating condition consistent across the core comparison unless a separate sensitivity study is retained.
- Restrict two-die TTV validation claims to the tested local geometry. Do not describe a two-die TTV as full 12-die validation.
- Replace all result placeholders only with completed, traceable simulation or measurement data.
