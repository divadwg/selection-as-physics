# Entropy, shared flow and inherited structure

Revised 9 September 2026. The original motivating question was whether life
maximises entropy production to compensate for its maintained order. The current
programme instead models competition for a share of supplied flow. It does not
assume a maximum-entropy-production principle. The [earlier ledger](entropy_ledger_before_audit.md)
is preserved, but several of its general claims were incorrect.

## What the fixed-boundary argument establishes

For an open system, counting heat, matter and radiation consistently,

```
dS_system/dt = entropy_in - entropy_out + entropy_produced,
entropy_produced >= 0.
```

At a stationary state the stored entropy does not change, so internal production
equals entropy out minus entropy in. If both boundary entropy flows are fixed,
rearranging the interior cannot change their difference. Different processes can
receive different portions of that budget. This does not specify which process
wins a competition or require that life maximise the total.

Fixed energy input or fixed effective infrared temperature alone is insufficient
to fix every entropy flow. Radiation entropy depends on the spectrum and angular
distribution; matter exchange and storage may also matter. Structure can change
absorption, atmospheric composition, emission and transport. A fixed-boundary
comparison deliberately holds these effects constant; it does not prove they
cannot occur. For ideal blackbody radiation Sdot=(4/3)*P/T; using it for the
whole Sun–Earth exchange is an approximation, not an exact planetary ledger.
See [Wu and Liu (2010)](https://doi.org/10.1029/2008RG000275).

The earlier claims that entropy is produced only when order degrades, that
chemical storage at temperature T has entropy per joule 1/T, and that every
complete ordering/decay cycle produces an identical entropy total are withdrawn.
Order can form in an irreversible process that produces entropy. The expression
Q/T concerns reversible heat transfer at a reservoir temperature, not a universal
entropy-to-energy ratio of chemical structures. Complete-cycle totals require
specified boundary exchanges and final states.

## Where entropy can enter the proposed sequence

| Step | Meaningful quantity | What the current models establish |
|---|---|---|
| Unequal flow sharing | Shannon entropy of shares; entropy production of state trajectories | Unequal shares can be quantified informationally, but that number is not thermodynamic entropy in joules per kelvin. The exact stationary state process obeys detailed balance. |
| Maintained structure | Dissipated power, free-energy storage, physical state lifetime | A physical flow can dissipate while maintaining a pattern. The channel variable alone does not specify its energy or entropy. |
| Reproduction | Usable work per viable offspring and physical irreversibility | The copying-cost threshold assumes a cost; it does not calculate that cost from thermodynamics. |
| Heredity and portable state | Parent–child information, error probability, work and dissipation | New assays quantify transmission. Physical copying and resetting rules are needed to connect fidelity to an entropy budget. |

There is a useful exact distinction at the first step. The conserved-flow model
has stationary density pi with zero probability current. Its validated event
process satisfies pi_x*k_xy=pi_y*k_yx. Therefore the standard stationary Markov
entropy-production expression

```
Sigma_coarse = (k_B/2) * sum_xy (pi_x*k_xy - pi_y*k_yx)
                              * log((pi_x*k_xy)/(pi_y*k_yx))
```

is zero. This applies to the resolved channel-state process, with the usual
state-reversal convention. It does not say that a physical apparatus carrying
the flow dissipates nothing: reservoirs, driven currents and unresolved variables
are not represented by those transitions. The concentration window consequently
cannot be interpreted as an entropy-production maximum of this process.

## Does sorting maximise anything?

The theorem fixes total throughput by construction. It does not derive that
constraint from entropy maximisation, or predict a monotonic increase in total
conductance, power, concentration or the share of a particular channel.
Zero disturbance freezes the initial channel states; equal channels are one
possible frozen start. Above the scaling window, extreme pooled concentration
fails in the defined joint limit, but equality need not return. Increasing a
common noise amplitude changes the clock, not the stationary law.

There is a mathematical convergence principle. If p is the current probability
density and pi the stationary density, the relative entropy
K=integral p log(p/pi) decreases under the reflected diffusion:

```text
dK/dt = -sum_i integral D_i p [partial_i log(p/pi)]^2 <= 0.
```

This follows by integration by parts with zero boundary current and the identity
partial_i(D_i*pi)=0. It describes approach of an ensemble distribution to its
stationary law. It does not say that a single trajectory is always becoming more
concentrated or that physical entropy production is maximised. Equivalently,
negative relative entropy is maximised at p=pi, but this mathematical rewriting
does not supply an independent physical objective or explain why that pi applies.
The noise and flow laws determine pi first.

For the proposed electrical test, fixed current is different from fixed power.
Parallel ohmic branches satisfy P=I_total^2/G_tot under current control. At equal
G_tot, redistributing conductance can change shares without changing power.
The [memristor assay note](memristor_q_analysis.md) keeps these boundary conditions
separate. We retain this interpretation here rather than adding an entropy
maximisation claim to either paper.

## Nonlinearity and a gate that stores memory

The earlier gate argument used two meanings. A stack of affine neural-network
layers without intervening nonlinearities is itself one affine map. Adding a
nonlinearity changes the class of possible input–output functions. This is an
algebraic statement, not a claim of topological inequivalence for every nonlinear
system. Nonlinearity alone does not imply memory, bistability or heredity.

A storage gate is more specific: a threshold or barrier protects a state against
small disturbances. The original memory simulation uses a threshold on writing.
The new continuous-carrier assay tests whether discrete storage is necessary for
finite-time transmission. It does not test an entirely linear world: its common
destination response contains tanh, and its reproductive allocation is normalized
by the population's total response. Thus it does not refute the original idea
that a nonlinearity may be needed somewhere in a proposed construction. Neither
test establishes that every nonlinear mechanism needs a discrete memory gate.

## The most useful thermodynamic extension

The next physical question is how much usable work is required to produce an
offspring with a specified fidelity and lifetime. It could make the existing
copying-cost and establishment threshold less arbitrary without assuming a
maximum of total entropy production.

A concrete test would give a carrier an energy landscape, a fuel-driven copying
reaction and reverse rates consistent with reservoir exchanges. It would account
for work and heat while measuring transmission errors and viable descendants.
Varying the copy protocol would then test whether the predicted establishment
boundary follows measured copying cost and fidelity. Finite-speed costs and
storage barriers need explicit models; there is no universal charge per turnover
of an unspecified pattern.

Landauer's familiar k_B*T*ln(2) bound applies to resetting an unbiased bit under
the usual assumptions. Logical copying into a prepared target need not itself
incur that universal dissipation; preparing/reusing targets and the full cycle
must be counted. [Bennett (2003)](https://arxiv.org/abs/physics/0210005).

Physical replication has thermodynamic bounds associated with its irreversibility,
internal entropy changes and reverse process:
[England (2013)](https://arxiv.org/abs/1209.1179). These are constraints, not proof
that selection universally maximises dissipation.

Biochemical copying can connect accuracy and dissipation under specified reaction
mechanisms: [Ouldridge, Govern and ten Wolde (2017)](https://arxiv.org/abs/1503.00909).
This is relevant prior art for turning the repository's assumed copying cost and
fidelity into physically accountable quantities. No such thermodynamic carrier
simulation is claimed in the current results.
