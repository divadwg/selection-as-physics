> Historical archive, superseded by [the heredity audit](heredity_audit.md)
> and [current derivations](derivations.md). Strong necessity and establishment
> claims below are preserved as history, not current conclusions.

# The four derivations (sketch rigour; hand-check before shipping)

Status: physicist-grade sketches with assumptions flagged. D1 is standard physics applied carefully; D2 assembles three known results with the wiring (physics ← factors) being the new content; D3 needs a concrete incumbent model; D4's establishment probability is a placeholder. Two new testable predictions fall out (end of file).

## D1. Dent-life from medium physics (condition 1's law)

Store a deviation h in a medium.
- Ungated (dial): dh/dt = −λh + ξ(t). Dent-life τ_dev = 1/λ. Polynomial in the healing rate: dials only slow forgetting (derives the memory-dial result).
- Gated (barrier ΔE): erasure requires an activation event. Kramers/Arrhenius: τ_dev = ν⁻¹·exp(ΔE/T_eff), with T_eff the effective noise temperature of local churn. Exponential persistence: derives the gate result.
- Coupling to the sorting axis: T_eff scales with local activity (the q-coupling, T_eff ∝ D(g) ∝ g^q locally), so busy sites erase their own marks faster. Heredity and sorting are not independent axes; high-flux locations trade persistence for revision.
- Condition 1 quantified: heritable variation exists iff ΔE > T_eff·ln(ν·τ_gen) (or, with copying, ν·τ_copy-wait).
- Assumptions: ΔE ≫ T_eff (Kramers validity); churn white on store timescales; linear healing for the dial case.

## D2. R₀ as physics (condition 3's law)

R₀ = (copy attempts per lifetime) × (per-copy success) = c·s · τ_dev · f.
- c·s: copy attempts funded by throughput share s (conservation law; the copying bridge, still an assumption, here isolated as the single bridge factor).
- τ_dev: maker lifetime = its store's dent-life, from D1 (death = erasure).
- f = f_copy · P(establish). Copy fidelity f_copy = exp(−μL) with mutation rate μ ∝ D ∝ g^q: Eigen's error threshold with the free parameter closed by the physics.
- R₀ = 1 is an explicit surface in (s, ΔE/T_eff, q): establishment threshold in the same coordinates as the sorting window. Survival of a single spark ≈ 2(R₀−1) near threshold (branching processes).
- Fizz picture: origination can be frequent with R₀ just below 1; failed-chain-length distribution measures distance to threshold; cycling environments cross episodically given storage (τ_dev spanning the bad phase).

### D0 (new, from review). The choice of stochastic variable
Multiplicative-noise SDEs are not invariant under change of variables: additive unbiased noise in one coordinate becomes state-dependent diffusion plus noise-induced drift in another. The theory must identify the physically natural variable in which elementary perturbations are additive and unbiased: Δg = Σ ε_k over N(J) events, E[ε]=0, giving D(g) = ½ r(g) σ²(g) in the diffusion limit. This is the physical derivation of state-dependent diffusivity, and the defence against the first expected attack.

### D2/D3 RESTRUCTURE (forced by sims/core/16-17): establishment is escape, then compounding
Copies inherit the parent's decaying trait, so offspring fates are correlated and no R0 (naive or trajectory-integrated) predicts survival. Correct two-stage law: (i) ESCAPE: some lineage member's trait must first-passage past the self-sustaining threshold before the family's shared decay absorbs it; copying's role while rare is multiplying escape attempts, P_surv ≈ 1 - (1 - p_esc)^M with M the family size before absorption; (ii) after escape, share is self-sustaining and compounding (R0 > 1) is automatic. R0 governs stage (ii) only. Superseding route (from review): branching diffusion in trait space. Extinction probability Q(g) obeys D(g)Q'' + v(g)Q' + b(g)(Q²−Q) + d(g)(1−Q) = 0; P_survive = 1−Q. One equation holds diffusion, drift, inheritance, copying, death; the escape threshold should emerge from its solution. Owed: solve (numerically first) with b ∝ J, d from erasure, D ∝ g^q, v = −k(g−g*); compare against sims/core/16-17 survival data.

## D3. Invasion at low share (the exponential-regime reachability theorem)

Incumbents: gradient-templated structures, produced at environment-set rate, no compounding; they overwrite replicator sites at rate δ. δ is re-templating one level up: the environment's pull exerted through the incumbent population.
- Replicator per-capita growth while rare: r = (R₀ − 1)/τ_gen.
- Invasion iff r > δ, i.e. **R₀ > 1 + δ·τ_gen**.
- The stable zoo (T10a) = the δ-dominated phase, derived.
- The recursion: v (variable level), healing λ (medium level), incumbent pressure δ (population level) are one object, the world re-imposing its template, at three scales; every threshold in the theory is a race against it.
- Owed: a concrete incumbent model fixing δ from the same physics (production rate of gradient structures per unit freed flux).

## D5 (new, from revised review). Copying derived from throughput: the accumulator
dA_i/dt = ηJ_i (throughput supplies usable work); copy when A_i ≥ E_copy (finite copy cost); hence τ_copy = E_copy/(ηJ) and b = ηJ/E_copy ∝ J, derived from two physical conditions rather than imposed. With inheritance g_daughter = g_parent + ε (ε from the same hidden layers), variation + heredity + differential reproduction follow, replicator/Price dynamics apply, and throughput plays two distinct roles from one conserved flow: engagement with hidden degrees of freedom (variation) and resource accumulation (reproduction). Demonstrated in-substrate (sims/core/18): emergent b(J) linear with slope ≈ 0.9·η/E (daughters start with empty accumulators), climb scaling inversely with copy cost, flat without copying.

## D4. Portability (condition 4's extension and the gating-necessity argument)

Add an advected state field a(x,t): ∂a/∂t + ∇·(u a) = writing − erasure, with configuration-addressed read (local D(g;a), v(g;a) depend on the a present, not its origin).
- Traveller's R₀ gains a transit factor: R₀_port = c·s · τ_dev · f · exp(−d/(u·τ_parcel)) · p_est(destination).
- Gating necessity on paper: ungated parcel τ_parcel = 1/λ (short) → transit survival dies exponentially with distance; gated parcel τ_parcel Kramers-long → transit survival ≈ 1. Gating is what makes distance affordable.
- Portability beats residence iff p_est(remote) > p_est(local)·exp(d/(u·τ_parcel)); for gated tokens the exponential ≈ 1 and the condition reduces to "less-contested substrate anywhere is worth going": the storage-economics conjecture as an inequality.
- Owed: p_est from D3's incumbent model; the two-variable stationary analysis.

## New predictions from the derivations (to test)

1. From D1's tension: dent-life falls with local activity. TESTED (sims/core/14): confirmed only in the churn-dominated regime (slope −0.16); flat where Q-independent healing dominates. Scope condition now part of D1: the tension applies where activity-churn dominates erasure.
2. From D4: gated vs ungated transit. TESTED (sims/core/15, and necessity closed in 17c: continuous parcels transmit nothing at any range while gated tokens are distance-flat; gating necessary and sufficient in the rung-3 world): direction confirmed and sharpened. A diffusive-accumulator gate gives quadratic-in-barrier persistence; Kramers-exponential requires a metastable well behind the barrier (D1's assumption made explicit). The dial's fidelity saturates at a noise floor as λ→0; the gate's rises without bound in ΔE. The operative distinction is tunability: gates can purchase arbitrary persistence, dials cannot.
3. From the R0 instrument (sims/core/16): naive branching theory fails under inherited decaying traits (correlated offspring fates); R0 must be evaluated along the re-templating trajectory. D2 to be amended: R0 = ∫ c·s(t)·f dt over the trait's decay path, not c·s·τ_dev with independent factors.


## D6 (from second-opinion critique). The window with drift: the matched calculation

The following is a scalar calculation, not a joint stationary law for a coupled population. From p ∝ (1/D)·exp(∫v/D), take v=a·g^s and D=d_0·g^q. The formulas below set d_0=1; otherwise replace a in the exponent and window shift by a/d_0:
- Subcritical (s < q−1): the exponential saturates at large g; tails unchanged; window verbatim.
- Marginal (s = q−1): exp(∫v/D) = g^a exactly, so q_eff = q − a and the window generalises to **1 + a ≤ q ≤ m + 1 + a**: both edges shift by the drift-to-noise ratio. Numerically verified (q=1.5, a=1.0 → de-concentrates, P_half 0.001 → 0.21; q=2.5, a=1.0 → rescued into the window, P_half 0.001). Drift can move systems into the window as well as out. Edges logarithmically soft at finite R, as at the undrifted margins.
- Supercritical positive drift (a > 0, s > q−1): scalar occupancy runs toward the cutoff; population and flow distributions coincide there (P_half approximately 0.5 in the independent-channel calculation). This does not establish takeover under a conserved total. The heterogeneous write-back/copying model in sims/core/05 is separate, and a general coupled drift result remains open. For a < 0, the tail is instead suppressed. Reinforcement v proportional to g^m is supercritical for q < m+1 and marginal at equality.

Owed follow-ups from the same critique: (a) coordinate-free statement of the theorem in terms of invariant observables (population fraction carrying half the flux), with exponents as chart-dependent bookkeeping; (b) the continuum-to-branching seam stated (p(g) is the sorting phase; countable lineages begin at establishment, where the branching diffusion takes over); (c) prior-art table (Yule-Simon, Büttiker/van Kampen, ratchets, England, autocatalytic sets, attachment-detachment inheritance models) with one line each on the difference; (d) finite-R behaviour presented from sims/core/04 rather than left as an R → ∞ idealisation; (e) the essay to show the sweep figure and link the repo.


## D7. Coupled finite-population stationarity

The independent stationary law is not exact for finite populations sharing a
conserved flow. For D_i=N g_i^q/S, S=sum(g_i^m), the zero-current joint law is
pi proportional to S product(g_i^(-q)). Consequently p_N=(1-1/N)p_0+f/N,
where f=g^m p_0/E_0[g^m]. Pooled flow retains density f. The pooled half-flow
population fraction is (1-1/N)P_0+1/(2N); the original window is recovered when
population size and state range grow. Snapshot concentration is a separate
observable. The proof, endpoint qualifications and numerical checks are in
[conserved_flow_validation.md](conserved_flow_validation.md).

This result does not establish the takeover assertion in D6. That section's
independent-channel upper-cutoff pileup and the heterogeneous write-back/copying
experiment are different models; a general coupled drift theorem remains owed.
