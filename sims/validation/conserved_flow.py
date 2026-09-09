"""Reflecting diffusion D_i = N*g_i**q/sum(g**m), with fixed total flow.

The simulator is an exact continuous-time nearest-neighbour Markov chain on
a uniform grid. Its generator converges to the Itô diffusion as the grid is
refined. No Euler steps, clipped overshoots, or capped event probabilities are
used. See docs/conserved_flow_validation.md for the stationary-law derivation.
"""

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Model:
    n: int = 8
    m: float = 1.0
    q: float = 1.0
    upper: float = 3.0
    intervals: int = 8

    def __post_init__(self):
        if self.n < 1 or self.intervals < 1 or self.upper <= 1 or self.m <= 0:
            raise ValueError("Require n >= 1, intervals >= 1, upper > 1, m > 0")

    @property
    def grid(self):
        return np.linspace(1.0, self.upper, self.intervals + 1)

    @property
    def spacing(self):
        return (self.upper - 1.0) / self.intervals


def stationary_marginals(model):
    """Return base occupancy, conserved occupancy, and pooled flow masses."""
    g = model.grid
    base = g ** (-model.q)
    base /= base.sum()
    flow = g ** (model.m - model.q)
    flow /= flow.sum()
    occupancy = (1 - 1 / model.n) * base + flow / model.n
    return base, occupancy, flow


def exact_samples(model, count, rng):
    """Sample the joint law S*prod(g_i**-q), using its mixture representation."""
    base, _, flow = stationary_marginals(model)
    states = rng.choice(len(base), size=(count, model.n), p=base)
    chosen = rng.integers(model.n, size=count)
    states[np.arange(count), chosen] = rng.choice(len(flow), size=count, p=flow)
    return states


def observables(model, states):
    """Equal-time occupancy and flow, plus the mean snapshot half-flow fraction.

    The last observable is deliberately distinct from the fraction of pooled
    occupancy above a pooled-flow quantile. It counts whole channels.
    """
    g = model.grid[states]
    weights = g ** model.m
    shares = weights / weights.sum(axis=1, keepdims=True)
    occupancy = np.bincount(states.ravel(), minlength=len(model.grid)) / states.size
    flow = np.bincount(states.ravel(), weights=shares.ravel(), minlength=len(model.grid))
    flow /= len(states)
    descending = np.sort(shares, axis=1)[:, ::-1]
    needed = 1 + np.sum(np.cumsum(descending, axis=1) < 0.5, axis=1)
    return occupancy, flow, float(np.mean(needed / model.n))


def initialize(model, count, kind, rng):
    if kind == "low":
        return np.zeros((count, model.n), dtype=int)
    if kind == "high":
        return np.full((count, model.n), model.intervals, dtype=int)
    if kind == "log_uniform":
        g = np.exp(rng.uniform(0, np.log(model.upper), (count, model.n)))
        return np.rint((g - 1) / model.spacing).astype(int)
    if kind == "stationary":
        return exact_samples(model, count, rng)
    raise ValueError(f"Unknown initial condition: {kind}")


def simulate(model, count, times, initial, seed, max_rounds=2_000_000):
    """Independent ensembles observed at fixed physical times.

    Each allowed +/- grid jump has rate N*g_i**q/(S*h**2). At an endpoint,
    the outward transition is absent (reflection). Sampling only jump states
    would bias occupancy; the exponential holding times here avoid that bias.
    The common factor N fixes time units and has no effect on stationarity.
    """
    times = np.asarray(times, dtype=float)
    if len(times) == 0 or times[0] < 0 or np.any(np.diff(times) <= 0):
        raise ValueError("Observation times must be nonnegative and strictly increasing")
    rng = np.random.default_rng(seed)
    states = initialize(model, count, initial, rng)
    clock = np.zeros(count)
    snapshots = []
    rounds = 0
    grid = model.grid
    for end in times:
        while True:
            active = np.flatnonzero(clock < end)
            if not len(active):
                break
            rounds += 1
            if rounds > max_rounds:
                raise RuntimeError("Event budget exhausted; no result claimed")
            x = states[active]
            g = grid[x]
            degrees = 2 - (x == 0).astype(int) - (x == model.intervals).astype(int)
            rates = model.n * g**model.q / (g**model.m).sum(axis=1, keepdims=True)
            rates *= degrees / model.spacing**2
            total = rates.sum(axis=1)
            next_time = clock[active] + rng.exponential(1 / total)
            jumping = next_time < end
            clock[active] = np.minimum(next_time, end)
            ids = active[jumping]
            if not len(ids):
                continue
            cumulative = np.cumsum(rates[jumping], axis=1)
            u = rng.random(len(ids)) * total[jumping]
            channel = np.minimum(np.sum(cumulative < u[:, None], axis=1), model.n - 1)
            old = states[ids, channel]
            step = np.where(rng.random(len(ids)) < 0.5, -1, 1)
            step = np.where(old == 0, 1, np.where(old == model.intervals, -1, step))
            states[ids, channel] += step
        snapshots.append(states.copy())
    return snapshots


def power_integral(exponent, upper):
    """Integral of g**exponent on [1, upper], stable near exponent = -1."""
    a = exponent + 1
    if abs(a) < 1e-12:
        return float(np.log(upper))
    return float(np.expm1(a * np.log(upper)) / a)


def continuum_half(m, q, upper):
    """Base population fraction above the continuum half-flow threshold."""
    if m <= 0 or upper <= 1:
        raise ValueError("Require m > 0 and upper > 1")
    a = m - q + 1
    threshold = np.sqrt(upper) if abs(a) < 1e-12 else ((1 + upper**a) / 2) ** (1 / a)
    b = 1 - q
    if abs(b) < 1e-12:
        return float(np.log(upper / threshold) / np.log(upper))
    # Integrate from threshold to upper directly to avoid subtracting nearly
    # equal CDFs when the requested tail fraction is tiny.
    tail = threshold**b * np.expm1(b * np.log(upper / threshold)) / b
    return float(tail / power_integral(-q, upper))


def pooled_half(occupancy, flow):
    """Fractional allocation of the threshold bin defines the grid quantile."""
    remaining = 0.5
    answer = 0.0
    for p, f in zip(occupancy[::-1], flow[::-1]):
        take = min(remaining, f)
        answer += p * take / f
        remaining -= take
        if remaining <= 1e-14:
            break
    return float(answer)
