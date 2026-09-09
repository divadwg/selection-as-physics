"""Constructive spatial examples, distinct from the conserved-flow theorem.

Runoff/erosion is a D8 landscape model; reaction--diffusion is the established
Gray--Scott model. Neither derives chemical reactions from molecular physics.
No operation detects a structure and instructs it to reproduce.
"""
from collections import deque
import numpy as np


def components(mask, periodic=False, min_size=1):
    labels = np.zeros(mask.shape, dtype=int)
    count = 0
    for i, j in zip(*np.where(mask)):
        if labels[i, j]:
            continue
        count += 1
        queue = deque([(i, j)])
        labels[i, j] = count
        while queue:
            x, y = queue.popleft()
            for a, b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if periodic:
                    a, b = a % mask.shape[0], b % mask.shape[1]
                if 0 <= a < mask.shape[0] and 0 <= b < mask.shape[1] and mask[a,b] and not labels[a,b]:
                    labels[a,b] = count
                    queue.append((a,b))
    sizes = np.bincount(labels.ravel())
    valid = [i for i in range(1, len(sizes)) if sizes[i] >= min_size]
    return labels, valid


def drainage(z, rain=None):
    """Strictly downhill routes; outlet row terminates flow, interior pits retain it."""
    nx, ny = z.shape
    if rain is None:
        rain = np.ones_like(z)/(nx-1)/ny
        rain[0] = 0
    index = np.arange(z.size).reshape(z.shape)
    dest = np.full(z.shape, -1, dtype=int)
    slope = np.zeros_like(z)
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == dy == 0:
                continue
            other = np.roll(np.roll(z,-dx,0),-dy,1)
            candidate = (z-other)/np.hypot(dx,dy)
            if dx == 1: candidate[-1] = 0
            if dx == -1: candidate[0] = 0
            if dy == 1: candidate[:,-1] = 0
            if dy == -1: candidate[:,0] = 0
            candidate[0] = 0
            better = candidate > slope
            slope[better] = candidate[better]
            dest[better] = np.roll(np.roll(index,-dx,0),-dy,1)[better]
    q = rain.ravel().copy()
    downstream = dest.ravel()
    for i in np.argsort(-z.ravel()):
        if downstream[i] >= 0:
            q[downstream[i]] += q[i]
    return q.reshape(z.shape), dest, slope


def landscape(exponent, seed=0, n=48, steps=600):
    rng = np.random.default_rng(seed)
    x = np.arange(n)[:,None]
    z = np.broadcast_to(.04*x,(n,n)).copy() + .003*rng.standard_normal((n,n))
    z[0] = 0
    initial = z.copy()
    q, dest, slope = drainage(z)
    ref = 1/n
    # Match initial total erosion between feedback and slope-only cases.
    rate = (q/ref)**exponent*slope
    k = .03*slope.sum()/rate.sum()
    records = []
    for t in range(steps+1):
        q, dest, slope = drainage(z)
        if t % 100 == 0 or t == steps:
            terminal = dest < 0
            pits = terminal.copy(); pits[0] = False
            records.append(dict(time=t, outlet_flow=float(q[0].sum()),
                retained_at_pits=float(q[pits].sum()), terminal_balance=float(q[terminal].sum()),
                top3_outlet_fraction=float(np.sort(q[0])[-3:].sum()/q[0].sum()),
                transverse_relief=float(np.std((z-z.mean(axis=1)[:,None])[1:])),
                mean_erosion=float((initial-z).mean()), erosion_coefficient=k))
        if t == steps: break
        flat_dest = dest.ravel(); drop=np.zeros(z.size); valid=flat_dest>=0
        drop[valid] = z.ravel()[valid]-z.ravel()[flat_dest[valid]]
        erosion = np.minimum(k*(q/ref)**exponent*slope,.25*drop.reshape(z.shape))
        z -= erosion
    return initial,z,q,records


def laplacian(a, dx=1.):
    return (np.roll(a,1,0)+np.roll(a,-1,0)+np.roll(a,1,1)+np.roll(a,-1,1)-4*a)/dx**2


def reaction_step(u,v,feed=.03,kill=.062,dt=1.,dx=1.,reaction=True):
    r = u*v*v if reaction else np.zeros_like(u)
    du = .16*laplacian(u,dx)-r+feed*(1-u)
    dv = .08*laplacian(v,dx)+r-(feed+kill)*v
    return u+dt*du, v+dt*dv


def gray_scott(seed=0, size=96., dx=1., dt=1., duration=4000., mode='seeded', amplitude=.01):
    """One prepared finite perturbation or small noise, followed by deterministic PDE steps.

Initial patch is one connected region, not a spatial array of descendants.
The feed is distributed reservoir exchange, not a fixed-total shared flux.
"""
    n = int(round(size/dx)); rng=np.random.default_rng(seed)
    u=np.ones((n,n));v=np.zeros((n,n))
    x,y=np.indices((n,n))*dx
    if mode in ('seeded','no_reaction','no_feed'):
        patch=(x-size/2)**2+(y-size/2)**2<25
        u[patch]=.5+amplitude*rng.uniform(-1,1,patch.sum())
        v[patch]=.25+amplitude*rng.uniform(-1,1,patch.sum())
    elif mode=='small_noise':
        v=amplitude*rng.random((n,n));u-=v
    elif mode!='unseeded':
        raise ValueError(mode)
    snapshots={};records=[]
    nsteps=int(round(duration/dt));stride=int(round(100/dt))
    for step in range(nsteps+1):
        if step%stride==0 or step==nsteps:
            t=step*dt
            row=dict(time=t, maximum=float(v.max()), total_v=float(v.sum()*dx**2),
                     minimum=float(min(u.min(),v.min())))
            for threshold in [.15,.2,.25]:
                _,valid=components(v>threshold,periodic=True,min_size=max(1,int(5/dx**2)))
                row[f'spots_{threshold}']=len(valid)
            records.append(row)
            if t in [0,200,400,600,1000,2000,4000]:snapshots[str(int(t))]=v.copy()
        if step==nsteps:break
        u,v=reaction_step(u,v,feed=0 if mode=='no_feed' else .03,dt=dt,dx=dx,reaction=mode!='no_reaction')
        if not np.isfinite(u).all() or min(u.min(),v.min()) < -1e-8:
            raise ArithmeticError('Nonfinite or negative concentration; reduce timestep')
    return records,snapshots
