"""Pilot: deterministic mixing maps drive the specified conserved-flow coupling.

The same area-preserving cat map acts on every hidden pair. Initial states are
randomized; evolution draws no random numbers. The state-dependent coupling is
supplied, not derived from microscopic transport. Small-step convergence must be
checked before identifying these bounded trajectories with the Ito theorem.
"""
import numpy as np


def hidden_step(x,y):
    return (2*x+y)%1.,(x+y)%1.


def reflect_box(g,lower=1.,upper=3.):
    width=upper-lower
    return lower+width-np.abs((g-lower)%(2*width)-width)


def simulate(q,dt,count=512,n=8,upper=3.,horizon=16.,seed=0):
    rng=np.random.default_rng(seed)
    x=rng.random((count,n));y=rng.random((count,n))
    g=np.full((count,n),(1+upper)/2)
    steps=round(horizon/dt)
    if not np.isclose(steps*dt,horizon):raise ValueError('Horizon must be an integer number of steps')
    prior=None; correlations=[]; checkpoints={}
    for t in range(steps):
        x,y=hidden_step(x,y)
        noise=np.sqrt(2)*np.cos(2*np.pi*x)
        diffusion=n*g**q/g.sum(axis=1,keepdims=True)
        g=reflect_box(g+np.sqrt(2*dt*diffusion)*noise,upper=upper)
        if prior is not None and t%32==0:correlations.append(float(np.mean(noise*prior)))
        prior=noise.copy()
        if t+1 in [steps//4,steps]:checkpoints[(t+1)*dt]=g.copy()
    return checkpoints,float(np.mean(correlations))
