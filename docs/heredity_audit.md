# From renewed patterns to inherited flow: current evidence

Revised 9 September 2026. This note supersedes the stronger heredity,
portability and establishment claims in the historical notes. It preserves the
original sequence: renewal of a pattern, reproduction of that pattern, then a
separate carrier that can recreate a property elsewhere. These are proposed
physical stages, not three established theorems.

## What was already in the repository

| Stage | Existing work | What can be concluded |
|---|---|---|
| Renewal through flow | The earlier README's heredity ladder; boundary experiments 01 and 05 | The models explore maintained loops and reconstruction from a persistent bed. Persistence of a shape is distinct from persistence of a particular perturbation. No new vortex simulation was run in this audit. |
| Local reproduction and memory | Core 10–12 | Copying can preserve state under a supplied copying rule. Channel junction correlations also reflect connected topography. A downstream confluence viewed backwards is not by itself an observed reproductive event. |
| Survival of a rare lineage | Core 16–17; derivations D2–D3 | The original founder counter was tied to a site, allowing later occupants to be confused with the founder. Script 16 now follows individual identity. Script 17 contains historical summaries, not executable follow-up experiments. |
| Portable information | Core 13 and 15 | Discrete tokens already travel and affect another site's response in a toy model. This is an implementation, not an unbuilt proposal. Its transport and expression laws are supplied. |

Core 13 labels transfers as downstream, but its flow is globally normalized
across sites rather than calculated through an advecting spatial field. Thus
remote expression there tests a supplied transfer rule, not spatial isolation
from all effects of the parent. The new packet assay likewise tests transfer
and response without claiming a resolved hydrodynamic transport model.

The Ship of Theseus analogy concerns continuity of organisation through material
turnover. For heredity of a variant, perturb the organisation and ask whether the
perturbation persists through renewal or reaches a descendant under matched
surroundings. For reproduction, record distinct parent and offspring identities.
For portable heredity, pass only the carrier and reconstruct the response in a
fresh site. A molecular carrier could be much simpler than DNA, and could itself
have catalytic activity. Chemistry that creates and copies it remains unspecified.

## New lineage calculation and independent simulation

[`sims/validation/heredity.py`](../sims/validation/heredity.py) implements a
continuous-time branching process on a finite trait lattice. Each individual
changes state with row generator T, attempts births at rate b, and disappears at
rate d. A copy from state i produces a viable daughter in state j with probability
P_ij; a row sum below one allows failed copies. The parent survives a birth.
Individuals behave independently conditional on their state in a fixed background.
This is an approximation for a rare lineage, not a finite-population takeover model.

The probability Q_i(t) of extinction by time t, starting from one individual, obeys

```
dQ/dt = T Q + b * Q * (P Q - P 1) + d * (1 - Q),    Q(0) = 0.
```

Here multiplication outside matrix products is elementwise. The expression in
parentheses is the daughter's extinction probability minus one. With perfect
inheritance P=Identity, the birth term is b*(Q²-Q). We integrate this equation,
refine its timestep, and compare it with independent exact-event simulations.
The eventual extinction probability is the minimal fixed point, obtained by
iteration from zero. Residuals are retained. Analytic one-state birth/death cases,
including failed copies, independently check the implementation.

We retain outcomes at times 2, 8 and 20, rather than equating survival at the last
time with survival forever. Reaching the computational cap is recorded as
censored: it contributes only to an upper bound on finite-time survival. Counts,
individual trial outcomes and parameters are in [the results](heredity_results/README.md).
The old experiment's claims of zero survival are finite-run observations, not
proofs of impossible establishment or failure of branching-process theory.

## The threshold and a candidate prediction

The expected number of offspring of each type is the matrix

```
K = (diag(d) - T)^(-1) diag(b) P.
```

For this finite, irreducible, nonsingular process, eventual survival has positive
probability when the largest eigenvalue in magnitude, rho(K), exceeds one.
This is established multitype branching mathematics. Inherited state does not
invalidate it. A simple count of one founder's births can miss the relevant
threshold because it ignores what kinds of descendants those births produce.

If b_i = eta*J_i/E_copy, the model predicts

```
E_copy < E_critical = eta * rho((diag(d)-T)^(-1) diag(J) P).
```

Thus measured flow, state transitions, disappearance and transmission can predict
a maximum viable copying cost. Actual waiting times from deterministic work
accumulators need an age/work state; the exponential birth clock here is an
additional assumption. The theorem's noise exponent alone does not fix T, d or P.
This formula is an application of known mathematics, not a new universal law.

The retained numerical example has g in [1,3], diffusion .02*g, restoration
-k*(g-1), disappearance .4, birth attempts c*g, and transmission success
exp(-.02*g*tau). The last rule assumes activity-dependent carrier damage and
counts a damaging event as a failed copy. It is not derived from channel noise,
and differs from the reversible-bit transport assay below. Transit survival is
applied at birth; an explicit travel delay is not simulated.

**Candidate prediction: restoring a channel toward a lower state can change
from hindering to helping establishment as transmission becomes more costly.**
Restoration sacrifices flow, but can reduce damage enough to improve viable
reproduction. We test the direction on 16, 32 and 64 intervals, compare both sides
of the copying threshold with simulated lineages, and include a control where
carrier damage is independent of g. This is a falsifiable prediction of the stated
couplings. We have not established that the reversal is new to the literature.
It neither follows from the stationary concentration window nor identifies that
window with the threshold for Darwinian selection.

For a fixed trait, viable births are c*g*exp(-.02*g*tau); their maximum occurs at
g=1/(.02*tau), if that point lies in [1,3]. This elementary balance explains why
the preferred trait can move downward as transit time grows. The matrix test
checks the balance when descendants also change state throughout their lives.

## Matched transport and repeated reproduction

The new assay gives each carrier the same initial value (+1 or -1), the same
transit time, and the same destination rule g=1+0.5*tanh(h). No original channel
state or stored work accompanies it. A binary carrier flips at rate .005. Two
continuous carriers follow an Ornstein–Uhlenbeck process with noise amplitude .1
and restoration rates .005 or .3. Exact transition laws avoid integration error.
These are specified storage laws, not equal-energy or equal-material comparisons.
We measure correlation, sign fidelity and the destination response on the same
scales, with a permutation null that preserves the received material distribution.

At transit time 40 the mean destination response difference between the two
source types is .510 for the binary carrier, .578 for the slow continuous carrier,
and approximately zero for the fast continuous carrier (10 seeds, 10,000 packets
per seed). Permutation-null effects are near zero. Gates can help maintain a
state; they are not necessary for all finite-time transmission. These runs cannot
rank storage technologies at matched physical cost or establish indefinite memory.

A separate finite-flow experiment replaces 256 sites over 40 generations. All
births pass only carrier state; each site's response is rebuilt. A pooled work
budget funds 256 copies of unit cost per generation under total flow one, so each
generation lasts 256 time units. Parent opportunities are proportional to flow,
or equal in a neutral control. This assumes reproduction and a common funding
pool; it does not derive local copying chemistry. Carrier transit time is a
parameter of the transmission law and is not added to the generation clock.

The final positive-state fractions, averaged over 20 seeds, are .919 (binary)
and .966 (slow continuous) with flow-weighted parent choice, versus .483 and .486
with equal parent opportunities. The fast continuous carrier ends near .5 in both
cases. All generation records and the work budget are retained.

The shuffled-pair null has exactly the same population trajectory as the faithful
case, but breaks the recorded parent–child association. It is a statistical null,
not a physical mechanism that abolishes heredity. Its agreement in population
means demonstrates why a rising mean alone cannot identify transmission: the
parent–child measurements are needed as well.

## What remains open

- A single deterministic physical construction connecting fine-scale fluctuations,
  inherited variation, the full concentration window and reproduction. The new
  checks use explicit random draws; they do not close this connection.
- Mechanistic reproduction of a spatial flow pattern with inherited variations.
  The current copying rules supply that ability.
- A physical carrier's creation, copying cost, error law and interaction with a
  destination. An aperiodic arrangement is a candidate, not a chemical mechanism.
- Feedback from a growing lineage onto the finite shared flow. The rare-lineage
  threshold predicts initial growth in a fixed background, not eventual takeover.
- A literature assessment of the candidate reversal. Prior work on ingredients
  neither establishes priority for this proposal nor proves the synthesis old.

Failures constrain a stated parameter regime and observation time. A zero count
in a finite sample does not prove zero probability, and a failed carrier model
does not exclude other storage mechanisms.

## Related evidence

Turbulent puffs split and decay in pipe flow, making reproduction versus loss a
physical comparison rather than just an analogy. That work does not establish
heredity of selectable variants or this conserved-flow mechanism:
[Lemoult and colleagues, Nature Physics (2024)](https://doi.org/10.1038/s41567-024-02513-0).

Autocatalytic RNA experiments distinguish reproduction from persistence of
composition: [Ameta and colleagues (2021)](https://doi.org/10.1038/s41467-021-21000-1).
Synthetic self-replicators selected for photocatalytic function offer a chemical
comparison: [Nature Catalysis (2025)](https://doi.org/10.1038/s41929-025-01409-3).
Neither is a test of the present noise window.

The use of extinction fixed points and offspring operators belongs to established
branching theory; see, for example, the finite-type discussion in
[Hautphenne, Latouche and Nguyen (2013)](https://arxiv.org/abs/1211.4129).

Reproduction–fidelity trade-offs have prior experimental treatment:
[a speed–fidelity trade-off in an RNA virus (2018)](https://doi.org/10.1371/journal.pbio.2006459).
The familiar existence of a trade-off should not be presented as the novelty.
