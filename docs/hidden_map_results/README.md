# Deterministic hidden dynamics: first controlled pilot

This pilot starts the connection between a deterministic hidden layer and the
stationary prediction in Paper 1. It keeps the hidden update rule unchanged while
varying the supplied state-dependent coupling below, inside and above the window.
It is a bounded numerical comparison, not a completed microscopic derivation or
physical validation. The original contact and seeding examples remain separate.

## Construction

Every route in every ensemble has a hidden pair (x,y). All pairs use the same
map on the unit torus:

```text
x_next = (2*x+y) modulo 1
y_next = (x+y) modulo 1
xi = sqrt(2)*cos(2*pi*x_next)
g_i_next = mirror_reflect(g_i + sqrt(2*dt*N*g_i^q/S)*xi_i)
S = sum_i g_i        (m=1 in this pilot).
```

The matrix has determinant one and an inverse with integer entries. With ideal
uniform initial conditions it preserves uniform measure. The cosine observable
has mean zero, variance one and zero autocovariance at every nonzero integer lag
under that ideal invariant measure: its Fourier mode and the iterated mode are
distinct. This does not make the sequence independent; the map is deterministic.
The implementation uses floating-point arithmetic, so the ideal continuous
measure argument is not a statement about indefinite finite-precision evolution.

Seeds initialise hidden states; every subsequent update is deterministic. Coarse
states all start at 2, not at their target stationary distribution. Different routes
have independent initial hidden pairs, with identical update rules. The coupling
sqrt(N*g_i^q/S) is explicitly supplied. This test does not derive that coupling
from growing contact counts or physical transport. It tests whether this specified
coupling driven by one unchanged deterministic substrate approaches the stationary
prediction. Deterministic homogenisation of multiplicative maps needs separate
conditions; see [Gottwald and Melbourne](https://arxiv.org/abs/1304.6222).

## Retained results

N=8, g in [1,3], m=1, q=.5/1.5/2.5; final physical time 16. Each setting has two
seeds with 512 independent ensembles per seed. The maximum absolute CDF error
is evaluated on 101 thresholds against the *continuous* exact stationary laws.
The table gives the larger final error of the two seeds.

| q | dt | Occupancy CDF error | Pooled-flow CDF error |
|---:|---:|---:|---:|
| .5 | 1/128 | .02363 | .01957 |
| .5 | 1/512 | .01892 | .01700 |
| 1.5 | 1/128 | .03044 | .02144 |
| 1.5 | 1/512 | .01528 | .01666 |
| 2.5 | 1/128 | .04149 | .03103 |
| 2.5 | 1/512 | .02383 | .01659 |

Reducing the step brings the worst errors closer to the target in these runs.
The finer-step maximum is .02383 for occupancy and .01700 for pooled flow.
These are observed discrepancies, not confidence intervals or a predeclared
acceptance threshold. Identical driver lag-one products across q confirm that
changing the coupling did not change the hidden trajectories. Their small size
is not a sufficient test of a white-noise limit or conditional drift.

`results.csv` retains times 4 and 16, per seed; NPZ files retain those full coarse
snapshots. `manifest.json` records settings and source hashes. No physical data
or large-range dynamical run is included.

The [subsequent calibration audit](../hidden_audit_results/README.md) measures
interior increments, predicts independent runs and widens the state range. It
retains the remaining drift concern. The following list records the gaps at
the time of this original pilot.

## What remains before strengthening the paper's claim

Measure conditional coarse drift, variance and cross-route correlations along
these trajectories, with boundary and temporal-memory effects accounted for.
Use further step refinement, different initial coarse states, longer observations
and larger state ranges to distinguish discretisation, incomplete relaxation
and sampling uncertainty. Then test the finite-range concentration curve itself,
not only its component CDFs. A short [1,3] run cannot demonstrate the limiting
vanishing-fraction classification. A failure of any one incomplete pilot would
not invalidate the broader physical proposal.

The independent-contact case q=m also needs an explicit bridge from interaction
allocation to the coupling. An independently calibrated physical realization is
still required to make a memristor claim. The present construction is deliberately
labelled a pilot rather than a completed solution of those gaps.

Reproduce from the repository root:

```sh
python -m sims.validation.run_hidden_map
python -m unittest tests.test_hidden_map
```

The runner overwrites these retained files. Three structural tests check the
hidden map's inverse, repeated-boundary reflection and deterministic reproduction
of finite trajectories. The repository suite had 29 tests when this pilot was completed.
