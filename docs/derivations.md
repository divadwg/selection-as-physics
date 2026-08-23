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

### D2/D3 RESTRUCTURE (forced by sims/core/16-17): establishment is escape, then compounding
Copies inherit the parent's decaying trait, so offspring fates are correlated and no R0 (naive or trajectory-integrated) predicts survival. Correct two-stage law: (i) ESCAPE: some lineage member's trait must first-passage past the self-sustaining threshold before the family's shared decay absorbs it; copying's role while rare is multiplying escape attempts, P_surv ≈ 1 - (1 - p_esc)^M with M the family size before absorption; (ii) after escape, share is self-sustaining and compounding (R0 > 1) is automatic. R0 governs stage (ii) only. Derivation owed: p_esc as a first-passage problem for a kicked, re-templated trait; M from the copying rate along the decay path.

## D3. Invasion at low share (the exponential-regime reachability theorem)

Incumbents: gradient-templated structures, produced at environment-set rate, no compounding; they overwrite replicator sites at rate δ. δ is re-templating one level up: the environment's pull exerted through the incumbent population.
- Replicator per-capita growth while rare: r = (R₀ − 1)/τ_gen.
- Invasion iff r > δ, i.e. **R₀ > 1 + δ·τ_gen**.
- The stable zoo (T10a) = the δ-dominated phase, derived.
- The recursion: v (variable level), healing λ (medium level), incumbent pressure δ (population level) are one object, the world re-imposing its template, at three scales; every threshold in the theory is a race against it.
- Owed: a concrete incumbent model fixing δ from the same physics (production rate of gradient structures per unit freed flux).

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
