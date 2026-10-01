"""Post-process V-die inter-die cooling study v3 results.

Inputs : results.csv (segment DOE), fulldie_results.csv (full-die baselines)
Outputs: figures (PNG/SVG) + summary CSVs in OUT.

Matched-pumping-power comparison:
  For each design, T-rise metrics are interpolated linearly in log10(pumping
  power) between the simulated velocities (no extrapolation).
Stack scaling (stated assumption): segment pumping power x (121 mm^2 / 2.88 mm^2)
  per gap x 39 gaps, i.e. every gap fed identically, manifold losses excluded.
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)

T_IN = 25.0
SEG_AREA = 1.2 * 2.4
SCALE_GAP = 121.0 / SEG_AREA
N_GAPS = 39

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Liberation Sans"],
    "font.size": 11, "axes.linewidth": 1.0,
    "xtick.direction": "out", "ytick.direction": "in",
    "xtick.top": False, "ytick.right": False,
    "axes.spines.top": True, "axes.spines.right": True,
    "axes.formatter.useoffset": False, "legend.frameon": False,
    "savefig.dpi": 300,
})


def blues(n):
    """Single blue hue, saturation stepped evenly by rank."""
    if n == 1:
        return ["#1f4e9c"]
    return [plt.cm.Blues(0.35 + 0.6 * i / (n - 1)) for i in range(n)]


df = pd.read_csv(SRC / "results.csv")
df = df[df["status"] == "OK"].copy()
df = df.drop_duplicates("case_id", keep="last")
df["dT_hot"] = df["T_hotspot_C"] - T_IN
df["dT_B"] = df["Tmax_dieB_C"] - T_IN
df["P_stack_W"] = df["pumping_power_W"] * SCALE_GAP * N_GAPS
df["key"] = df["design"] + "_g" + df["gap_um"].astype(int).astype(str) + "_m" + df["mesh_resolution"].astype(str)


def label(r):
    if r["design"] == "empty":
        s = "No pillar"
    else:
        arr = "staggered" if r["arrangement"] == "staggered" else "in-line"
        s = f"d{int(r['pillar_diameter_um'])}/p{int(r['pillar_pitch_um'])} µm, {arr}"
    return s + f", gap {int(r['gap_um'])} µm"


df["label"] = df.apply(label, axis=1)
df.to_csv(OUT / "segment_results_clean.csv", index=False)

main = df[df["mesh_resolution"] == 4]
groups = {k: g.sort_values("pumping_power_W") for k, g in main.groupby("key")}


def interp_at(g, col, p):
    x = np.log10(g["P_stack_W"].values)
    if len(g) < 2 or not (x.min() <= np.log10(p) <= x.max()):
        return np.nan
    return float(np.interp(np.log10(p), x, g[col].values))


# ---- matched-pumping-power table at gap 175 and all gaps ----
rows = []
p_grid = [0.5, 1.0, 2.0, 5.0]
for k, g in groups.items():
    r0 = g.iloc[0]
    for p in p_grid:
        rows.append(dict(key=k, label=r0["label"], gap_um=r0["gap_um"], P_stack_W=p,
                         dT_hotspot=interp_at(g, "dT_hot", p),
                         dT_dieB=interp_at(g, "dT_B", p),
                         dT_die_die=interp_at(g, "dT_die_die_max_C", p),
                         dp_Pa=interp_at(g, "dp_Pa", p)))
mp = pd.DataFrame(rows)
mp.to_csv(OUT / "matched_pumping_power.csv", index=False)


def style(ax):
    ax.tick_params(which="both", top=False, right=False)
    ax.tick_params(axis="x", which="both", direction="out")
    ax.tick_params(axis="y", which="both", direction="in")


# ---- Fig 1: hotspot rise vs stack pumping power (gap 175) ----
for gap in sorted(main["gap_um"].unique()):
    sel = {k: g for k, g in groups.items() if g.iloc[0]["gap_um"] == gap}
    if not sel:
        continue
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8))
    order = sorted(sel, key=lambda k: (sel[k].iloc[0]["design"] != "empty", k))
    cols = blues(len(order))
    for c, k in zip(cols, order):
        g = sel[k]
        ls = "--" if g.iloc[0]["design"] == "empty" else "-"
        mk = "s" if g.iloc[0]["arrangement"] == "staggered" else "o"
        axes[0].plot(g["P_stack_W"], g["dT_hot"], ls, marker=mk, color=c,
                     label=g.iloc[0]["label"].split(", gap")[0])
        axes[1].plot(g["P_stack_W"], g["dT_die_die_max_C"], ls, marker=mk, color=c)
    for ax, yl in zip(axes, ["Hotspot temperature rise (K)", "ΔT$_{die-die}$ (K)"]):
        ax.set_xscale("log")
        ax.set_xlabel("Pumping power, 40-die stack (W)")
        ax.set_ylabel(yl)
        style(ax)
    axes[0].legend(fontsize=8.5, loc="upper right")
    fig.suptitle(f"Inter-die gap {int(gap)} µm, inlet 25 °C, 3 W/die + I/O hotspot", fontsize=10)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig1_T_vs_pump_gap{int(gap)}.{ext}")
    plt.close(fig)

# ---- Fig 2: pressure drop vs velocity ----
fig, ax = plt.subplots(figsize=(4.8, 3.8))
order = sorted(groups, key=lambda k: (groups[k].iloc[0]["gap_um"], groups[k].iloc[0]["design"] != "empty", k))
for c, k in zip(blues(len(order)), order):
    g = groups[k].sort_values("velocity_m_s")
    ax.plot(g["velocity_m_s"], g["dp_Pa"] / 1e3, "-o", color=c, ms=4, label=g.iloc[0]["label"])
ax.set_xlabel("Inlet velocity (m/s)")
ax.set_ylabel("Δp over 2.4 mm segment (kPa)")
ax.legend(fontsize=6.5)
style(ax)
fig.tight_layout()
for ext in ("png", "svg"):
    fig.savefig(OUT / f"fig2_dp_vs_velocity.{ext}")
plt.close(fig)

# ---- Fig 3: full-die top-side vs inter-die ----
fd_path = SRC / "fulldie_results.csv"
if fd_path.exists():
    fd = pd.read_csv(fd_path)
    fd = fd[(fd["status"] == "OK") & (fd["Tmax_die_C"] < 500)]
    fd = fd.drop_duplicates(["mode", "velocity_m_s"], keep="last")
    fd.to_csv(OUT / "fulldie_clean.csv", index=False)
    if len(fd):
        fig, ax = plt.subplots(figsize=(4.8, 3.8))
        labels, tmax, tavg = [], [], []
        for _, r in fd.sort_values(["mode", "velocity_m_s"]).iterrows():
            labels.append("Top-side\ncold plate" if r["mode"] == "topside"
                          else f"Inter-die flow\n{r['velocity_m_s']:g} m/s")
            tmax.append(r["Tmax_die_C"] - T_IN)
            tavg.append(r["Tavg_die_C"] - T_IN)
        x = np.arange(len(labels))
        c = blues(2)
        ax.bar(x - 0.18, tmax, 0.36, color=c[1], label="T$_{max}$ rise")
        ax.bar(x + 0.18, tavg, 0.36, color=c[0], label="T$_{avg}$ rise")
        for xi, v in zip(x, tmax):
            ax.text(xi - 0.18, v, f"{v:.1f}", ha="center", va="bottom", fontsize=8)
        ax.set_xticks(x, labels, fontsize=9)
        ax.set_ylabel("Die temperature rise above 25 °C (K)")
        ax.set_title("11 × 11 mm die, 3 W/die, 200 µm Si", fontsize=10)
        ax.legend(fontsize=9)
        style(ax)
        fig.tight_layout()
        for ext in ("png", "svg"):
            fig.savefig(OUT / f"fig3_topside_vs_interdie.{ext}")
        plt.close(fig)

print(mp.to_string())

# ---- Fig 4: die-count scaling in a fixed stack length (analytic, anchored) ----
# Top-side: 1D fin with uniform generation, ideal isothermal top edge:
#   dT_max = P*H / (2*k*W*t)  (validated against Icepak at t = 200 um: see fulldie_clean.csv)
# Inter-die: simulated full-die value at t = 200 um held constant with N (estimate;
#   heat leaves locally through the die faces, so it depends weakly on t).
if fd_path.exists() and len(fd):
    STACK_MM = 40 * 0.200 + 39 * 0.175
    GAP = 0.175
    k, H, W = 148.0, 11e-3, 11e-3
    N = np.arange(30, 71)
    t = (STACK_MM - (N - 1) * GAP) / N * 1e-3
    top = fd[fd["mode"] == "topside"]
    inter = fd[(fd["mode"] == "interdie")].sort_values("velocity_m_s")
    fig, ax = plt.subplots(figsize=(4.8, 3.8))
    c = blues(3)
    for P, ls in ((3.0, "-"),):
        ax.plot(N, T_IN + P * H / (2 * k * W * t), ls, color=c[2], label=f"Top-side cold plate ({P:g} W/die, analytic)")
    if len(top):
        ax.plot([40], top["Tmax_die_C"].values[:1], "o", color=c[2], mfc="white", label="Top-side, Icepak (N = 40)")
    if len(inter):
        r = inter.iloc[0]
        ax.plot(N, np.full_like(N, r["Tmax_die_C"], dtype=float), "--", color=c[0],
                label=f"Inter-die flow {r['velocity_m_s']:g} m/s (Icepak at N = 40)")
    for lim in (85, 95):
        ax.axhline(lim, color="0.5", lw=0.8, ls=":")
        ax.text(N[-1], lim + 1, f"{lim} °C", ha="right", fontsize=8, color="0.4")
    ax.set_xlabel(f"Number of dies in a {STACK_MM:.1f} mm stack (gap 175 µm)")
    ax.set_ylabel("Peak die temperature (°C)")
    ax.set_ylim(20, 160)
    ax.legend(fontsize=7.5, loc="upper left")
    style(ax)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"fig4_die_count_scaling.{ext}")
    plt.close(fig)
