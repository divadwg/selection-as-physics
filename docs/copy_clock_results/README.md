# Copying clocks and lifetime output

The second paper compares two specified clocks with the same mean attempt rate
for an immortal parent. An empty accumulator must receive each copy's work before
attempting it. A Poisson clock at that nominal rate can attempt a copy arbitrarily
early and is not an equivalent work-conserving model.

For usable power W, copy cost E, viable same-capability daughter probability p,
and irreversible loss of copying ability at rate mu:

```text
Accumulator: R = p / (exp(mu E/W) - 1); critical E = W log(1+p) / mu
Poisson:     R = Wp / (mu E);           critical E = Wp / mu
```

The parent remains after attempts. Every newborn starts empty and has the same
independent life-history law. These assumptions give a standard branching
genealogy: positive eventual survival requires R>1. The result does not derive
physical copying, equate physical object lifetime with copying-state lifetime,
or predict indefinite growth with finite total resources. Failed attempts cost
work too. These are applications of established renewal and branching mathematics.
[Stukalin et al. (2013)](https://doi.org/10.1098/rsif.2013.0325) provide relevant
prior work on why age-dependent reproduction cannot generally be replaced by
constant birth and death rates; originality for this comparison is not claimed.

`results.csv` contains six settings, each with 100,000 independent explicit event
histories. W=mu=1 and p=.8. The raw NPZ files contain each parent's loss time,
attempt count and viable daughter count. Seeds and source hashes are in
`manifest.json`. The expected probability of zero offspring, also retained, is
1/(1+R) for these particular geometric offspring distributions. This follows from
geometric completed intervals before exponential loss (accumulator), or a Poisson
count mixed over an exponential lifetime, followed by Bernoulli thinning.

At E=.7 the expected outputs are .7891 for the accumulator and 1.1429 for Poisson;
the observed means are .7836 (SE .0037) and 1.1355 (SE .0049). All six mean errors
are below two estimated standard errors; this is not a simultaneous confidence
claim. The simulations test lifetime reproduction, not whole genealogical survival.
The branching criterion follows analytically from the independent offspring law.
The retained accumulator histories never spend unreceived work.

Reproduce from the repository root:

```sh
python -m sims.validation.run_copy_clock
python -m unittest tests.test_copy_clock
```

The runner overwrites these results. NumPy is the only numerical dependency.
Three tests check the survival-weighted sum, the opposite classifications at
E=.7 and lifetime work accounting. The full repository suite has 26 tests.
