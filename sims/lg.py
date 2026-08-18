"""
Stage 1: does a gradient-driven lattice flow form closed loops above a threshold,
and does it need the momentum nonlinearity to do so?

Substrate: D2Q9 lattice Boltzmann (the ensemble-averaged lattice gas). Tokens are
population densities on 9 velocity channels per cell. Collisions conserve mass and
momentum. Drive: fixed inflow velocity at left edge, open outflow at right edge.
Obstacle: a disc. Control parameter: Reynolds number (drive / viscosity).

Two variants:
  full   : standard collision (equilibrium quadratic in u) -> momentum carried
  linear : equilibrium truncated at first order in u -> no momentum advection
"""
import numpy as np, sys, json

# lattice
cx = np.array([0, 1, 0,-1, 0, 1,-1,-1, 1])
cy = np.array([0, 0, 1, 0,-1, 1, 1,-1,-1])
w  = np.array([4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36])
opp= np.array([0,3,4,1,2,7,8,5,6])

def equilibrium(rho, ux, uy, linear=False):
    cu = 3*(cx[:,None,None]*ux + cy[:,None,None]*uy)
    if linear:
        return w[:,None,None]*rho*(1 + cu)
    usq = 1.5*(ux**2 + uy**2)
    return w[:,None,None]*rho*(1 + cu + 0.5*cu**2 - usq)

def run(Re, nx=300, ny=90, r=9, u0=0.05, steps=8000, linear=False, seed=0, record_from=None):
    nu  = u0*2*r/Re
    tau = 3*nu + 0.5
    if tau < 0.51:  # stability guard
        raise ValueError(f"tau={tau:.3f} too small for Re={Re}; lower u0 or enlarge r")
    omega = 1.0/tau
    X, Y = np.meshgrid(np.arange(nx), np.arange(ny), indexing='ij')
    cxo, cyo = nx//5, ny//2 + 0.5   # slight offset breaks symmetry
    solid = (X-cxo)**2 + (Y-cyo)**2 < r*r
    rng = np.random.default_rng(seed)
    ux = np.zeros((nx,ny)); uy = np.zeros((nx,ny))
    rho = np.ones((nx,ny))
    f = equilibrium(rho, ux, uy, linear)
    if record_from is None: record_from = steps//2
    probe = (int(cxo + 4*r), ny//2)
    ts = []
    for t in range(steps):
        rho = f.sum(0)
        ux  = (cx[:,None,None]*f).sum(0)/rho
        uy  = (cy[:,None,None]*f).sum(0)/rho
        # inflow: impose velocity (ramped up over first 2000 steps, tiny noise to break symmetry), outflow: zero gradient
        uin = u0*min(1.0, t/1000.0)
        ux[0,:] = uin*(1 + 1e-3*rng.standard_normal(ny)); uy[0,:] = 0
        feq = equilibrium(rho, ux, uy, linear)
        f = f - omega*(f - feq)
        # inlet: fixed density 1, imposed velocity; outlet: copy from neighbour
        f[:,0,:] = equilibrium(np.ones((1,ny)), ux[0:1,:], uy[0:1,:], linear)[:,0,:]
        f[:,-1,:] = f[:,-2,:]
        # bounce back at obstacle
        fs = f[:, solid]
        f[:, solid] = fs[opp]
        # stream
        for i in range(9):
            f[i] = np.roll(np.roll(f[i], cx[i], axis=0), cy[i], axis=1)
        if t >= record_from:
            ts.append(uy[probe])
    # vorticity field
    om = (np.gradient(uy, axis=0) - np.gradient(ux, axis=1))
    om[solid] = 0
    ts = np.array(ts)
    # attached recirculation: any reversed flow in the wake means a closed loop exists
    xc = int(cxo)
    wake = ux[xc+r:xc+4*r, :]
    reversed_frac = float((wake < -0.05*u0).mean())
    return dict(reversed_frac=reversed_frac, Re=Re, tau=tau, ux=ux, uy=uy, om=om, solid=solid, ts=ts,
                probe_amp=float(ts.std()), linear=linear)

def count_loops(om, solid, thresh_frac=0.25, min_sep=6):
    """count local |vorticity| maxima downstream of obstacle above a fraction of the max"""
    a = np.abs(om)
    thr = thresh_frac*a.max()
    from scipy.ndimage import maximum_filter
    peaks = (a == maximum_filter(a, size=2*min_sep+1)) & (a > thr) & (~solid)
    # ignore the shear layer glued to the obstacle: require x beyond obstacle centre + 2r
    xs = np.argwhere(peaks)
    xc = np.argwhere(solid)[:,0].mean()
    return int((xs[:,0] > xc + 18).sum())

if __name__ == "__main__":
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    Res = [5, 20, 40, 60, 80, 110]
    results = []
    for Re in Res:
        r = run(Re)
        r['nloops'] = count_loops(r['om'], r['solid'])
        results.append(r)
        print(f"Re={Re:4d} tau={r['tau']:.3f} probe amp={r['probe_amp']:.2e} loops={r['nloops']} reversed_frac={r['reversed_frac']:.3f} nan={np.isnan(r['ux']).any()}", flush=True)
    # linear control at highest drive
    lin = run(110, linear=True)
    lin['nloops'] = count_loops(lin['om'], lin['solid'])
    print(f"LINEAR Re=110 probe amp={lin['probe_amp']:.2e} loops={lin['nloops']} reversed_frac={lin['reversed_frac']:.3f}", flush=True)

    # figure 1: vorticity panels
    fig, axes = plt.subplots(len(Res)+1, 1, figsize=(10, 1.6*(len(Res)+1)))
    for ax, r in zip(axes, results+[lin]):
        v = np.abs(r['om']).max() + 1e-12
        ax.imshow(r['om'].T, cmap='RdBu_r', vmin=-v, vmax=v, origin='lower', aspect='auto')
        tag = "LINEAR (no momentum term) " if r['linear'] else ""
        ax.set_ylabel(f"{tag}Re={r['Re']}", fontsize=8, rotation=0, ha='right', va='center')
        ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle("Vorticity (loops) in a driven lattice flow past a disc. Red/blue = opposite circulation.")
    fig.tight_layout()
    fig.savefig("/mnt/user-data/outputs/loops_vs_drive.png", dpi=110)

    # figure 2: threshold plot
    fig, ax = plt.subplots(1,2, figsize=(9,3.2))
    ax[0].plot(Res, [r['probe_amp'] for r in results], 'o-')
    ax[0].axhline(lin['probe_amp'], color='gray', ls='--', label='linear control, Re=110')
    ax[0].set_xlabel("Re (drive / viscosity)"); ax[0].set_ylabel("oscillation of transverse velocity\ndownstream (loop shedding)")
    ax[0].set_yscale('log'); ax[0].legend(fontsize=8)
    ax[1].plot(Res, [r['nloops'] for r in results], 's-')
    ax[1].axhline(lin['nloops'], color='gray', ls='--')
    ax[1].set_xlabel("Re"); ax[1].set_ylabel("distinct vortex cores downstream")
    fig.tight_layout()
    fig.savefig("/mnt/user-data/outputs/threshold.png", dpi=110)

    summary = [dict(Re=r['Re'], tau=round(r['tau'],3), probe_amp=r['probe_amp'], loops=r['nloops'], reversed_frac=r['reversed_frac'], linear=r['linear']) for r in results+[lin]]
    json.dump(summary, open("/mnt/user-data/outputs/summary.json","w"), indent=1)
