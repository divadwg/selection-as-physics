"""
Does a blinking gradient build structure that a steady one does not?
Fast field u (flux, e.g. heat) diffuses from a source edge to a sink edge.
Slow field s (material) at each cell: more material -> the cell releases its u more slowly (capacity).
Material is deposited in proportion to flux passing through, and decays at a fixed rate (maintenance).
Identical rules in both runs. Only the drive schedule differs: steady at half strength, or on/off at full.
"""
import numpy as np
def run(mode, nx=60, ny=40, steps=6000, period=400, D=0.2, a=0.02, b=0.002, seed=0, gate=None):
    rng=np.random.default_rng(seed)
    u=np.zeros((nx,ny)); s=0.05*rng.random((nx,ny))
    hist=[]; sink_total=0.0
    for t in range(steps):
        drive = 0.5 if mode=='steady' else (1.0 if (t//period)%2==0 else 0.0)
        u[0,:]=drive
        # release rate per cell
        rel=D/(1+s)
        out=rel*u                       # amount each cell can pass this step
        # split equally to 4 neighbours (diffusion-like), no wrap in x, wrap in y
        inflow=np.zeros_like(u)
        for ax,sh in ((0,1),(0,-1),(1,1),(1,-1)):
            q=np.roll(out,sh,axis=ax)/4
            if ax==0 and sh==1: q[0,:]=0
            if ax==0 and sh==-1: q[-1,:]=0
            inflow+=q
        u=u-out+inflow
        sink_total+=u[-1,:].sum(); u[-1,:]=0     # sink
        u[0,:]=drive
        # material: deposited by throughput, decays
        thru=out
        s=s+a*thru-b*s
        if gate is not None: s=np.where(s<gate,0.0,s)   # optional threshold: below gate, material does not persist
        if t%200==0 or t==steps-1:
            hist.append((t,float(s.std()),float(s.mean()),float(u.mean()),sink_total))
    return u,s,hist,sink_total
if __name__=="__main__":
    import json
    out={}
    for mode in ['steady','rhythm']:
        u,s,h,tot=run(mode); out[mode]=dict(s=s.tolist(),u=u.tolist(),hist=h,sink=tot)
        print(mode,'final s mean',round(s.mean(),3),'s std',round(s.std(),3),'std/mean',round(s.std()/s.mean(),3),'flux delivered to sink',round(tot,1))
    json.dump(out,open('/home/claude/rhythm.json','w'))
