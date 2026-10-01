import sys, pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
U=sys.argv[1]
plt.rcParams.update({"font.family":"sans-serif","font.sans-serif":["Arial","Liberation Sans"],"font.size":10.5,
 "xtick.direction":"out","ytick.direction":"in","xtick.top":False,"ytick.right":False,"legend.frameon":False,"savefig.dpi":300,"axes.formatter.useoffset":False})
e=pd.read_csv(f"{U}/vdie10_empty_manual_nomlm_r2_l25_v0p5_man25um_gc3/per_die.csv")
p=pd.read_csv(f"{U}/vdie10_pillar_manual_nomlm_r2_l25_v0p5_man25um_gc3/per_die.csv")
t=pd.read_csv(f"{U}/vdie10_topside_manual_nomlm_man25um_gc7/per_die.csv")
c=[plt.cm.Blues(v) for v in (0.45,0.7,0.95)]
fig,ax=plt.subplots(1,2,figsize=(9.6,3.8),gridspec_kw=dict(width_ratios=[1,1.6]))
lab=["Top-side\ncold plate","Inter-die flow\nno pillar","Inter-die flow\nCu pillar"]
tm=[t.Tmax_C.max()-25,e.Tmax_C.max()-25,p.Tmax_C.max()-25]
ax[0].bar(range(3),tm,color=[c[2],c[1],c[0]],width=0.6)
for i,v in enumerate(tm): ax[0].text(i,v,f"{v:.1f}",ha="center",va="bottom",fontsize=9)
ax[0].set_xticks(range(3),lab,fontsize=9); ax[0].set_ylabel("Peak die temperature rise (K)")
ax[0].set_title("10-die stack, 3 W/die + I/O hotspot",fontsize=10)
x=np.arange(10)
for df,col,l,m in ((e,c[1],"No pillar","o"),(p,c[2],"Cu pillar (I/O zone)","s")):
    ax[1].plot(x,df.Tmax_C-25,"-",marker=m,color=col,label=f"{l}: die T$_{{max}}$")
    hs=df.dropna(subset=["T_hotspot_C"])
    ax[1].plot(hs.die,hs.T_hotspot_C-25,":",marker=m,mfc="white",color=col,label=f"{l}: I/O hotspot")
ax[1].set_xticks(x); ax[1].set_xlabel("Die index (even = active with I/O hotspot)")
ax[1].set_ylabel("Temperature rise above 25 °C (K)"); ax[1].legend(fontsize=8,loc="upper center",ncol=2)
ax[1].set_ylim(1.4,3.4)
for a in ax: a.tick_params(top=False,right=False)
fig.tight_layout(); fig.savefig("fig5_10die_comparison.png"); fig.savefig("fig5_10die_comparison.svg")
