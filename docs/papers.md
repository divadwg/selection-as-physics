# Papers and research directions

## Current draft

[A finite noise window for concentration of a shared flow](../paper/finite_noise_window.pdf),
David Galbraith, revised 9 September 2026.
[Source, figure data and build instructions](../paper/README.md).

The paper studies one reflected, driftless Itô model with a fixed shared flow.
It derives the exact joint stationary law, the finite-population correction and
the precise pooled concentration window. It then develops the proposed route
from deterministic fine-scale disturbance to selection through explicit lattice
and copying thought experiments. [Retained example runs](research_examples/README.md)
make their evidence and limitations inspectable. The upper edge is presented as an
application of established moment mathematics, without a priority claim for
the threshold itself. It is a working draft, not a peer-reviewed publication.

The numerical evidence is the bounded coupled validation suite. Published
fluctuation exponents and exploratory substrate models are not empirical
validation. The discontinued aggregate-nanowire route supplies no verdict.

## Work beyond this paper

The repository also contains models of copying funded by throughput, memory
refresh, lineage establishment and transport of stored state. Each introduces
additional assumptions. The paper discusses the first steps in this programme; further extensions
remain separate research directions rather than parts of the stationary theorem.

A physical test would require states and flows resolved by channel, a fixed total,
checks of the joint variance rule and drift, and adequate relaxation and state
range. Until such a test is available, the broader synthesis remains a hypothesis.

The earlier paper specification is preserved in Git history. It overstated
several links between the window, preferential attachment and empirical exponent
placements, and is superseded by the current draft.
