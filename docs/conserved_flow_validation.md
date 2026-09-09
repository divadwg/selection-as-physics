# Stationarity with a conserved total flow

This note replaces the claim that independent walkers verify the finite-population,
conserved-flow model. It gives an exact stationary law for a specified coupled
model, checks that law with a separate event simulation, and states which limit
recovers the noise window. It does not establish the model as a description of a
particular physical system.

## Model and boundaries

There are N channels with states g_i in [1,R], m > 0, and independently driven
Itô noise. Define

    S(g) = sum_i g_i^m
    J_i = I g_i^m / S(g)
    D_i(g) = N g_i^q / S(g)
    dg_i = sqrt(2 D_i(g)) dW_i

with reflection at both ends of the interval and no interior drift. The total
flow is exactly I in every configuration. The factor N fixes time units and does
not affect the stationary law. On q=m, the diffusivity is proportional to the
actual channel flow. Off that line, this specifies a common normalization of
noise by S. A different rule, such as D_i proportional to J_i^(q/m), has a different
normalization and is not covered by the formula below.

The older forty-route code approximates the q=m dynamics when its additive kicks
are small and its event probabilities remain below one. It also lacks a fixed
upper reflecting boundary. The bounded stationary model studied here is therefore
a defined limit to compare with that toy, not an exact description of every
parameter setting or of its unbounded transient growth.

## Joint stationary law

Write

    p_0(g) = g^(-q) / Z,       Z = integral_1^R g^(-q) dg
    mu = integral_1^R g^m p_0(g) dg
    f(g) = g^m p_0(g) / mu.

The normalized joint stationary density is

    pi(g_1,...,g_N) = S(g) / (N mu) * product_i p_0(g_i).

For each coordinate, D_i pi is independent of g_i. Consequently every probability
current -partial_i(D_i pi) vanishes, including the reflecting-boundary current.
The density is positive and normalizable on the bounded box. The diffusion is
nondegenerate there, so this is its unique invariant probability density.

An equivalent construction is to choose one channel uniformly, sample its state
from f, and sample all other states independently from p_0. Averaging over the
chosen channel gives exactly pi. This supplies an independent sampler for checks
of observables involving the whole configuration.

The tagged-channel occupancy is therefore

    p_N(g) = (1 - 1/N) p_0(g) + (1/N) f(g).

The mean total flow distribution across state is

    E_pi[sum_i (J_i/I) delta(g-g_i)] = f(g).

Thus the conserved model has the same pooled flow density as the independent
calculation, but a finite-N correction to occupancy. For example, with one channel
and q=m, D_1 is constant and occupancy is uniform. The independent-channel formula
p_0 proportional to g^(-m) would be wrong for that system.

These identities hold equally for a uniform state lattice when integrals are
replaced by sums. The tests also enumerate all configurations of a three-channel,
three-state chain and check detailed balance on every edge.

## Half-flow observable and the limits

Let a_R be the threshold above which half the pooled flow lies, so that
integral_a_R^R f = 1/2. Let P_0(R) = integral_a_R^R p_0. Then

    P_N(R) = (1 - 1/N) P_0(R) + 1/(2N).

For exact powers, P_0(R) tends to zero as R tends to infinity precisely when
1 <= q <= m+1. Inside that window, fixed N gives P_N -> 1/(2N), not zero. Taking
N to infinity as well removes the correction and recovers the original window.
For this pooled observable and this model, either iterated limit gives that same
classification; finite-N corrections remain relevant to actual measurements.
The fixed-R stationary N->infinity limit also restores the independent marginal.

This pooled quantile is not the mean fraction of channels required to carry half
the flow in an individual snapshot. The latter counts whole channels, is at least
1/N, and depends on the joint law. The suite measures it separately and compares
it with independent samples of pi. Neither observable establishes persistence of
the identities of particular winners.

For m=1 and q=2, P_0=1/(sqrt(R)+1). At R=10^8 and N=40, the pooled fraction is
about 0.012598, whereas the independent prediction is about 0.000100. The correction
is small in absolute population fraction but large relative to this tail quantity.

## The endpoints require more than slopes

The inclusive window above assumes exact powers (or suitably strong asymptotic
equivalence). A limiting log-log slope alone does not determine the endpoints.
For example, on g>=e, J=g and D=g^2(log g)^2 have m=1 and limiting q=2, but
integral J/D converges. The claimed upper-edge tail separation then fails.
The strict inequalities are robust to such logarithmic factors; the endpoints
require checking the actual integrals.

## Numerical method and reproduction

From the repository root, with Python 3.10 or later:

    python -m pip install -r requirements-validation.txt
    python -m unittest discover -s tests -v
    python -m sims.validation.run_validation

Only NumPy is required. The runner writes CSV data and an environment/version
summary into docs/validation_results. Defaults are N=8, R=3, three seeds, and 128
independent ensembles per seed. It covers (m,q)=(1,0.5), (1,1), (1,1.5), (1,2),
(1,2.5), and (2,4). Each case starts at the lower boundary, upper boundary, a
log-uniform distribution, and the exact stationary distribution. Observations are
at physical times 0, 1, 4, and 16. The stationary start is a maintenance control;
the other starts test relaxation. Each row retains its seed and observation time.

The simulation is a continuous-time nearest-neighbour chain. Every allowed jump
of channel i by one grid spacing h has rate

    N g_i^q / (S h^2).

Outward boundary jumps are absent. The next event is selected by its rate and
occurs after an exponential holding time. Ensembles are observed at fixed physical
times, not at event counts. This simulates the grid chain without a time-step
approximation or an event-probability cap. Its interior generator approximates D_i times the second derivative; excluding
outward jumps gives reflection in the continuum limit as h decreases. The finite grid itself remains an
approximation to continuous state.

The checks report maximum absolute CDF errors for occupancy and pooled flow, and
absolute error in the mean snapshot half-flow fraction. The snapshot reference
uses 100,000 independent joint-law samples per exponent pair. A declared tolerance
of 0.05 is applied to all final errors. It is an acceptance threshold, not a
confidence interval. The CSV retains transient failures; the runner exits with an
error if its final criterion fails.

The grid-refinement table compares exact stationary grid quantiles with the
continuum answer at 4 through 256 intervals. The population-limit table evaluates
the analytic finite-N correction over R=10^2 through 10^8 and N=8 through 4000.
Those tables are mathematical evaluations, not simulations over those large ranges.
To check relaxation on a finer grid separately:

    python -m sims.validation.run_validation --intervals 8 --output docs/validation_results/finer_grid

The retained forty-channel check uses the same initial conditions and exponents:

    python -m sims.validation.run_validation --channels 40 --intervals 8 --output docs/validation_results/forty_channels

Results: [default grid](validation_results/README.md),
[finer grid](validation_results/finer_grid/README.md), and
[forty channels](validation_results/forty_channels/README.md).

The retained results test bounded systems with specified parameters. They do not
establish a universal equilibration time, convergence rates at large R, or empirical
validity of the constitutive rules. They also do not imply winner-take-all under
positive drift; that needs a separate coupled analysis.

## Why the previous SDE check was insufficient

The earlier script initialized g=exp(Uniform(0,log R)), already the desired density
for q=1. Agreement at q=1 to four figures therefore checked maintenance, not
relaxation from a different distribution. Its 20,000 steps at dt=0.001 cover only
20 time units. At the original N=200,000 and q=0.5, a rerun returned fitted q about
0.95 and a half-flow fraction 0.1012, against the stationary prediction 0.2130.
That run had not equilibrated. For large q, its single reflection followed by
clipping also permits discretization artefacts when jumps span the interval.

The old numerical experiment remains available only as a labelled legacy diagnostic.
The exact power-law integration remains valid. The new coupled validation replaces
the unsupported interpretation of the independent-walker run.
