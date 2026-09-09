"""Controlled lineage and carrier models, separate from the stationary theorem.

The branching approximation holds the environment fixed while a lineage is rare.
Carrier models prescribe storage, transmission and expression; they do not derive
chemical copying or the origin of a carrier. All randomness here is explicit.
"""
from dataclasses import dataclass
import numpy as np


@dataclass
class Branching:
    transition: np.ndarray  # Row generator for the state of a living individual.
    birth: np.ndarray       # Birth adds one individual in the parent's current state.
    death: np.ndarray
    offspring: np.ndarray | None = None  # Substochastic: missing mass is a failed copy.

    def __post_init__(self):
        n = len(self.birth)
        if self.offspring is None:
            self.offspring = np.eye(n)
        if self.offspring.shape != (n,n) or np.any(self.offspring < 0) or np.any(self.offspring.sum(axis=1) > 1+1e-12):
            raise ValueError('Invalid offspring probabilities')
        if self.transition.shape != (n, n) or self.death.shape != (n,):
            raise ValueError('Incompatible state dimensions')
        off = self.transition - np.diag(np.diag(self.transition))
        if np.any(off < 0) or np.any(self.birth < 0) or np.any(self.death <= 0):
            raise ValueError('Rates must be nonnegative, with positive death rates')
        if not np.allclose(self.transition.sum(axis=1), 0):
            raise ValueError('Transition rows must sum to zero')

    def rhs(self, q):
        child_extinction = 1-self.offspring.sum(axis=1) + self.offspring@q
        return self.transition @ q + self.birth * q*(child_extinction-1) + self.death*(1-q)

    def extinction(self, horizon, dt=0.005):
        """P(extinct by horizon), RK4 solution of the backward equation, Q(0)=0."""
        count = max(1, int(np.ceil(horizon/dt)))
        step = horizon/count
        q = np.zeros(len(self.birth))
        for _ in range(count):
            a = self.rhs(q)
            b = self.rhs(q + step*a/2)
            c = self.rhs(q + step*b/2)
            d = self.rhs(q + step*c)
            q += step*(a+2*b+2*c+d)/6
        if np.any(q < -1e-9) or np.any(q > 1+1e-9):
            raise ArithmeticError('Invalid probability; refine integration step')
        return q

    def eventual_extinction(self, tolerance=1e-12, max_steps=200000):
        """Minimal fixed point from zero; also returns its equation residual."""
        off = self.transition - np.diag(np.diag(self.transition))
        rate = self.birth + self.death - np.diag(self.transition)
        q = np.zeros(len(rate))
        for _ in range(max_steps):
            child_extinction = 1-self.offspring.sum(axis=1) + self.offspring@q
            nxt = (off@q + self.birth*q*child_extinction + self.death)/rate
            if np.max(np.abs(nxt-q)) < tolerance:
                return nxt, float(np.max(np.abs(self.rhs(nxt))))
            q = nxt
        raise ArithmeticError('Extinction fixed point did not converge')

    def reproduction_radius(self):
        # Expected time in each state before death, times births in that state.
        kernel = np.linalg.solve(np.diag(self.death)-self.transition,
                                 np.diag(self.birth)@self.offspring)
        return float(max(abs(np.linalg.eigvals(kernel))))

    def trial(self, initial, horizon, seed, cap=128):
        """Exact Gillespie counts. A cap hit is censored, never called survival."""
        rng = np.random.default_rng(seed)
        counts = np.zeros(len(self.birth), dtype=int)
        counts[initial] = 1
        off = self.transition - np.diag(np.diag(self.transition))
        rates = self.birth + self.death + off.sum(axis=1)
        time = 0.0
        while counts.sum():
            if counts.sum() >= cap:
                return 'censored'
            total = float(counts@rates)
            time += rng.exponential(1/total)
            if time > horizon:
                return 'alive_at_horizon'
            i = int(rng.choice(len(counts), p=counts*rates/total))
            u = rng.random()*rates[i]
            if u < self.birth[i]:
                probabilities = np.append(self.offspring[i], 1-self.offspring[i].sum())
                j = int(rng.choice(len(counts)+1, p=probabilities))
                if j < len(counts):
                    counts[j] += 1
            elif u < self.birth[i]+self.death[i]:
                counts[i] -= 1
            else:
                j = int(rng.choice(len(counts), p=off[i]/off[i].sum()))
                counts[i] -= 1
                counts[j] += 1
        return 'extinct'


def trait_model(copy_rate=0.22, restoring=0.4, intervals=8):
    """Reflecting trait lattice, diffusion D=.02*g, restoration toward g=1."""
    g = np.linspace(1, 3, intervals+1)
    step = g[1]-g[0]
    transition = np.zeros((len(g), len(g)))
    for i, value in enumerate(g):
        if i:
            transition[i, i-1] = .02*value/step**2 + restoring*(value-1)/step
        if i+1 < len(g):
            transition[i, i+1] = .02*value/step**2
    transition -= np.diag(transition.sum(axis=1))
    return g, Branching(transition, copy_rate*g, np.full(len(g), .4))


def transmit(h, mode, distance, rng, decay=None, sigma=.1, flip_rate=.005):
    """Analytically sampled storage laws; distance equals transit time at speed 1.

Gated: binary symmetric continuous-time flips. Dial: exact OU transition.
The comparison is conditional on these rates, not equal physical storage costs.
"""
    h = np.asarray(h, dtype=float)
    if mode == 'gated':
        flip = rng.random(h.shape) < -np.expm1(-2*flip_rate*distance)/2
        return np.where(flip, -h, h)
    if mode not in ('slow_dial', 'fast_dial'):
        raise ValueError(mode)
    lam = decay if decay is not None else (.005 if mode == 'slow_dial' else .3)
    variance = sigma*sigma*distance if lam == 0 else sigma*sigma*(-np.expm1(-2*lam*distance))/(2*lam)
    return np.exp(-lam*distance)*h + np.sqrt(variance)*rng.standard_normal(h.shape)


def response(h):
    """Same bounded conductance response at a fresh site for every carrier."""
    return 1 + .5*np.tanh(h)


def transfer_assay(mode, distance, seed, samples=10000):
    rng = np.random.default_rng(seed)
    source = rng.choice([-1., 1.], samples)
    landed = transmit(source, mode, distance, rng)
    child = response(landed)
    # Preserve the entire distribution of material and landing effects, break ancestry.
    shuffled = child[rng.permutation(samples)]
    return dict(correlation=float(np.corrcoef(source, landed)[0, 1]),
                sign_fidelity=float(np.mean(np.sign(landed) == source)),
                response_effect=float(child[source > 0].mean()-child[source < 0].mean()),
                shuffled_effect=float(shuffled[source > 0].mean()-shuffled[source < 0].mean()))


def generations(mode, control, seed, n=256, count=40, distance=10, total_flow=1., copy_cost=1.):
    """Finite-flow, fixed-size generational replacement with portable state.

Each generation lasts n*copy_cost/total_flow. The common work budget funds n
births. Birth opportunities go to parents by flow, or equally in the neutral
control. This is a prescribed pooled funding mechanism, not local accumulators.
Only h is passed; every destination's g is reconstructed from h. Permuting the
same packets breaks ancestry while preserving aggregate population behaviour.
"""
    if control not in ('faithful', 'shuffled', 'neutral'):
        raise ValueError(control)
    rng = np.random.default_rng(seed)
    shuffle_rng = np.random.default_rng(seed+100000)
    h = np.tile([-1., 1.], n//2)
    if len(h) != n:
        raise ValueError('Use an even population')
    rows = []
    for generation in range(1, count+1):
        g = response(h)
        flow = total_flow*g/g.sum()
        p = np.full(n, 1/n) if control == 'neutral' else flow/total_flow
        parents = rng.choice(n, n, p=p)
        source = h[parents]
        child = transmit(source, mode, distance, rng)
        paired = child if control != 'shuffled' else child[shuffle_rng.permutation(n)]
        corr = float(np.corrcoef(source, paired)[0, 1]) if np.std(source)>0 and np.std(paired)>0 else None
        rows.append(dict(generation=generation, positive_fraction=float(np.mean(child > 0)),
                         mean_response=float(response(child).mean()), parent_child_corr=corr,
                         total_flow=float(flow.sum()), work_in=n*copy_cost,
                         work_spent=n*copy_cost, duration=n*copy_cost/total_flow))
        # Sites are exchangeable. Sorting permits a paired comparison with the
        # shuffled ancestry control without changing either population law.
        h = np.sort(child)
    return rows
