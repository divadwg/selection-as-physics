"""Lifetime reproduction under two specified copying clocks.

The accumulator pays a fixed cost before every attempt. The Poisson comparison
has the same attempt rate for an immortal parent, but allows early attempts and
is not a pathwise work-conserving empty-store model. Both assume copying exists.
"""
import numpy as np


def reproduction(work, cost, loss, fidelity, clock='accumulator'):
    if work <= 0 or cost <= 0 or loss <= 0 or not 0 <= fidelity <= 1:
        raise ValueError('Require positive work rate, cost and loss, and fidelity in [0,1]')
    if clock == 'accumulator':
        return fidelity/np.expm1(loss*cost/work)
    if clock == 'poisson':
        return fidelity*work/(loss*cost)
    raise ValueError('Unknown clock')


def offspring(work, cost, loss, fidelity, clock, count, seed):
    """Independent individual life histories, with event times explicitly generated."""
    reproduction(work, cost, loss, fidelity, clock)
    rng = np.random.default_rng(seed); lifetime = rng.exponential(1/loss, count)
    times = np.zeros(count); attempts = np.zeros(count, dtype=int); viable = np.zeros(count, dtype=int)
    alive = np.arange(count); spacing = cost/work
    while len(alive):
        times[alive] += spacing if clock == 'accumulator' else rng.exponential(spacing, len(alive))
        alive = alive[times[alive] < lifetime[alive]]
        attempts[alive] += 1
        viable[alive] += rng.random(len(alive)) < fidelity
    return lifetime, attempts, viable
