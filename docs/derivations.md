# Derivations and their current scope

Revised 9 September 2026. The [previous sketches](derivations_before_heredity_audit.md)
are preserved as history. Several necessity and threshold claims there were too
strong. The [heredity audit](heredity_audit.md) is the current account.

## Concentration of a conserved flow

For the reflected driftless model D_i=N*g_i^q/S, S=sum(g_i^m), the exact
stationary density is proportional to S*product(g_i^(-q)). The pooled flow law
and finite-population correction follow in
[the model derivation](conserved_flow_validation.md). Under the specified power
laws, the limiting window is 1 <= q <= m+1. This is a concentration result,
not a necessary-and-sufficient condition for every form of selection.

## Persistence of a state

A linear store dh=-lambda*h*dt+sigma*dW retains its conditional mean with factor
exp(-lambda*t). Its variance also matters for recoverable information. A barrier
can lengthen persistence; a Kramers exponential requires an appropriate metastable
potential and weak-noise assumptions. A diffusive accumulator hitting a threshold
is not automatically a Kramers model. Neither digital storage nor infinite
persistence is necessary for transmission across a finite distance.

State renewal, inheritance across births and portable information are separate
questions. The current [matched carrier checks](heredity_results/README.md)
include a continuous carrier that succeeds over the tested times.

## Copying funded by flow

If a store receives usable work eta*J and a copy costs E, its ideal long-run
copying rate is eta*mean(J)/E, subject to losses and unused remainder. This is
conditional on a physical copying process and efficiency. Core 18 implements
such an accumulator with stochastic state changes and replacement; it is not a
joined deterministic substrate. A birth/death process with exponential waiting
times is a different approximation, tested explicitly below.

## Establishment of a rare lineage

Let T describe trait transitions while alive, d disappearance rates, and P
viable offspring types per birth attempt. The next-generation matrix is
K=(diag(d)-T)^(-1)*diag(b)*P. Under the finite irreducible branching assumptions,
rho(K)>1 gives positive eventual survival probability. Inheritance requires
tracking offspring types; it does not make branching theory inapplicable.

For b=eta*J/E, this supplies the model-specific threshold
E_critical=eta*rho((diag(d)-T)^(-1)*diag(J)*P). Extinction probabilities, finite-time
survival and independent event simulations are in the [audit](heredity_audit.md).
Finite-population competition and accumulator ages are not included in this
fixed-background approximation. If incumbent pressure is already in d, adding
it again as a separate loss threshold would double-count it.

## Transport and the candidate reversal

The retained extension assumes P_ii=exp(-.02*g_i*tau), with a damaged copy leaving
no viable daughter. It predicts that restoration toward lower g can hinder
establishment for short transit and help for long transit. A state-independent
damage control isolates the assumed coupling. Numerical grid sensitivity and
both sides of the threshold are retained. This is a conditional prediction,
not an established novelty claim or a new general theorem of selection.

## Drift in a scalar model

For scalar diffusion, zero current gives p proportional to
D^(-1)*exp(integral(v/D)). With D=d0*g^q and v=a*g^(q-1), the power exponent shifts
by a/d0. This does not supply a joint stationary law for a coupled drifting
population or prove takeover. The earlier scalar calculations remain in the
historical sketches with that limitation.
