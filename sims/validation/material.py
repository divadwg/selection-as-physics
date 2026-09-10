"""Conservative binary cohesion coupled to fluid reflection on a substrate.

This is a deterministic zero-temperature relaxation construction, not a thermal
Kawasaki sampler or a momentum-conserving simulation of a freely suspended solid.
The substrate absorbs momentum and heat. The fluid does not erode the material.
"""
import numpy as np
from sims.boundaries.lg import cx, cy, opp, equilibrium


def bonds(bits):
    """Occupied nearest-neighbour pairs, counted once on a periodic grid."""
    return int(sum(np.count_nonzero(bits & np.roll(bits, -1, axis=a)) for a in (0, 1)))


def exchange_gain(bits, x, y, axis):
    """Change in occupied bonds if one nearest-neighbour pair exchanges."""
    nx, ny = bits.shape
    xx, yy = ((x+1) % nx, y) if axis == 0 else (x, (y+1) % ny)
    a, b = int(bits[x, y]), int(bits[xx, yy])
    if a == b:
        return 0
    def neighbours(i, j):
        return sum(int(bits[k, l]) for k, l in
                   (((i-1) % nx, j), ((i+1) % nx, j), (i, (j-1) % ny), (i, (j+1) % ny)))
    return (b-a)*(neighbours(x, y)-b-neighbours(xx, yy)+a)


class Material:
    def __init__(self, bits, block=4, cohesive=True):
        self.bits = np.asarray(bits, dtype=bool).copy()
        if min(self.bits.shape) < 3 or any(n % block for n in self.bits.shape):
            raise ValueError('Grid must have at least three sites per axis and divide into blocks')
        self.block, self.t, self.cohesive = block, 0, cohesive

    def coarse(self):
        nx, ny = self.bits.shape; b = self.block
        return self.bits.reshape(nx//b, b, ny//b, b).mean(axis=(1, 3))

    def sweep(self):
        """Visit initially unlike bonds in a deterministic, time-varying order.

        Moves accept non-increasing H=-bonds. Neutral exchanges allow isolated
        particles and flat interfaces to move. New unlike bonds wait a sweep.
        The integer ordering is an update schedule, not a physical noise law.
        """
        bits = self.bits; nx, ny = bits.shape
        candidates = np.concatenate([np.flatnonzero(bits != np.roll(bits, -1, axis=a)) + a*nx*ny
                                     for a in (0, 1)])
        # An explicit integer permutation avoids random draws during evolution.
        keys = (candidates.astype(np.uint64) + np.uint64(self.t*104729))
        keys = ((keys ^ (keys >> 16))*np.uint64(0x45d9f3b)) & np.uint64(0xffffffff)
        keys = ((keys ^ (keys >> 16))*np.uint64(0x45d9f3b)) & np.uint64(0xffffffff)
        keys ^= keys >> 16
        accepted = 0
        for index in candidates[np.argsort(keys, kind='stable')]:
            axis, site = divmod(int(index), nx*ny); x, y = divmod(site, ny)
            xx, yy = ((x+1) % nx, y) if axis == 0 else (x, (y+1) % ny)
            if bits[x, y] != bits[xx, yy] and (not self.cohesive or exchange_gain(bits, x, y, axis) >= 0):
                bits[x, y], bits[xx, yy] = bits[xx, yy], bits[x, y]
                accepted += 1
        self.t += 1
        return accepted


def initial_material(nx=180, ny=60, r=6, block=4, seed=0, dispersed=False):
    """Prepared dense irregular patch; dispersed control preserves its exact mass."""
    rng = np.random.default_rng(seed)
    x, y = np.indices((nx*block, ny*block))
    x = (x+.5)/block; y = (y+.5)/block
    angle = np.arctan2(y-(ny/2+.5), x-nx//5)
    radius = r*(1+.13*np.sin(3*angle)+.08*np.cos(5*angle))
    bits = (np.hypot(x-nx//5, y-(ny/2+.5)) < radius) & (rng.random(x.shape) < .88)
    if dispersed:
        count = int(bits.sum()); bits[:] = False
        bits.flat[rng.choice(bits.size, count, replace=False)] = True
    return Material(bits, block)


def reflect(f, fraction):
    """Local convex mixing: preserves mass and multiplies momentum by 1-2s."""
    return (1-fraction)*f + fraction*f[opp]


class MaterialFlow:
    def __init__(self, material, re=40, r=6, u0=.03, coupled=True):
        self.material = material; self.nx, self.ny = material.coarse().shape
        self.r, self.u0, self.coupled = r, u0, coupled
        self.tau = .5+3*u0*2*r/re
        self.f = equilibrium(np.ones((self.nx, self.ny)), np.zeros((self.nx, self.ny)),
                             np.zeros((self.nx, self.ny)))
        self.t = 0

    def velocity(self):
        rho = self.f.sum(0)
        return (cx[:, None, None]*self.f).sum(0)/rho, (cy[:, None, None]*self.f).sum(0)/rho

    def step(self, n):
        f = self.f; ny = self.ny
        fraction = self.material.coarse() if self.coupled else np.zeros((self.nx, ny))
        for _ in range(n):
            rho = f.sum(0)
            ux = (cx[:, None, None]*f).sum(0)/rho; uy = (cy[:, None, None]*f).sum(0)/rho
            uin = self.u0*min(1., self.t/1000.)
            ux[0] = uin; uy[0] = 0
            f -= (f-equilibrium(rho, ux, uy))/self.tau
            f[:, 0, :] = equilibrium(np.ones((1, ny)), ux[:1], uy[:1])[:, 0, :]
            f[:, -1, :] = f[:, -2, :]
            f = reflect(f, fraction)
            for i in range(9):
                f[i] = np.roll(np.roll(f[i], cx[i], axis=0), cy[i], axis=1)
            f[:, 0, :] = equilibrium(np.ones((1, ny)), np.full((1, ny), uin), np.zeros((1, ny)))[:, 0, :]
            f[:, -1, :] = f[:, -2, :]
            if not np.isfinite(f).all() or f.sum(0).min() <= 0:
                raise ArithmeticError('Flow became unstable')
            self.t += 1
        self.f = f
