# Natural selection as physics

*This README is the argument. Records live in `docs/` (experiments, derivations, references, ledger, history, essay), code in `sims/`, figures in `figures/`. Pre-rewrite versions are preserved in `docs/` for the record.*

---

## 0. The claim

Everything that persists in a flow is a pattern the flow keeps re-making. On a fixed energy input the total entropy production is set by the input, not by what stands in the way: structure changes flux, inputs and routes, never entropy per joule of output. Order does not cost extra entropy up front; entropy is produced when order degrades, not when it is created. So the only thing patterns in a shared flow can compete over is share of the flow, and the question "is natural selection physics?" becomes precise: under what conditions does sharing a conserved flow, plus the noise of layers too fine to see, produce Darwin's phenomenon?

The answer here is one stationary law with four conditions read off it, plus one derived bridge from flow to reproduction. Where the conditions hold, a minimal Darwinian regime follows within this model class, and both constitutive relations that previous versions assumed are now derived from stated physical conditions: state-dependent noise from growth geometry, and copying rate from throughput-funded work against a finite copy cost. Each condition is separately checkable, each has a failure regime, and real systems can be placed on the resulting diagram from measured exponents. Pre-copying, everything the theorems deliver is *sorting* in Vrba and Gould's sense, differential persistence, not selection; the write-ups say sorting until copying is explicitly in place.

## 1. The law

Any coarse variable g (a channel's width, a filament's conductance, a firm's capacity) is driven by layers its own description cannot resolve. Mori-Zwanzig makes the consequence exact: the unresolved layers deliver both moments of their influence at once, a fluctuating part with diffusivity D(g) = ½ · r(g) · σ²(g) (event rate times kick size squared), and a mean part v(g), the re-templating pull back toward whatever the drive and geometry dictate. Kicks are the mutation; the pull is the forgetting; one source, two moments. Stationary occupancy is

**p(g) ∝ (1/D(g)) · exp(∫ v/D)**

and with share of a conserved flux J(g) ∝ g^m and D(g) ∝ g^q, the flux-weighted density is ∝ g^(m−q). Four conditions are read off this one object:

1. **Heredity**: the pull is weak enough that deviations outlive the timescale on which they matter.
2. **Sorting**: the diffusivity's growth with state sits in a finite window, and the noise differs between individuals.
3. **Establishment**: a rare replicating lineage escapes the pull before its correlated family is absorbed.
4. **Portability**: state can travel without its carrier, which requires gating.

Orthogonality: heredity without sorting is neutral wander (genetic drift is exactly the flat-noise control); sorting without heredity is a zoo of perfectly re-templated types, sorted and going nowhere. Both are needed and neither implies the other.

## 2. Condition 1: heredity is weak re-templating

A deviation (a dent in the state) survives only if it outlives the pull: dent-life must exceed a generation, or, with copying, the waiting time until the state is next copied. Fast fields fail this; a whirlpool's perturbations contract within a few turnovers, so it remembers its type and never its scars. Slow stores pass it, and the good stores are *gated*: a barrier converts the hidden layers' influence from (mean pull, continuous jitter) into (mean ≈ 0, rare discrete kicks). Gating is the v-killer, which is why heredity-capable media are the gated ones and why storage generically goes digital; Weismann's split falls out as soma = fast field, germline = gated store.

Status. The dent-life law is sketched (Kramers: dials give persistence linear in 1/λ and only ever slow forgetting; gates give persistence rising without bound in barrier height; docs/derivations.md D1), with a measured scope condition: busy sites erase their own marks faster only where activity-churn dominates erasure (sims/core/14). Re-templating erases the sorting inversion, run as a labelled consistency check (11). The non-obvious and confirmed result is that **copying is memory refresh**: with copying, a deviation need only survive until it is copied, so the population climb survives re-templating that kills sorting alone, the rescue scales with copy rate, and it fails exactly where copy-interval reaches dent-life; since copying is funded by share, fitness itself buys heritability (12).

## 3. Condition 2: sorting is a finite window on the noise

With v ≈ 0, occupancy is p ∝ g^(−q) while flux density is ∝ g^(m−q). Count individuals and the population piles where jitter is least; count flux and it sits with the few disturbed most. The two censuses separate, a vanishing fraction of the population carrying a dominant fraction of the throughput, exactly when

**1 ≤ q ≤ m + 1**

with both edges marginal: below the window nothing concentrates, above it the high states are emptied so hard that even the flux ends up low. Equivalently, the window is a moment-divergence window for a physically generated heavy-tailed stationary distribution. The noise must also be idiosyncratic: kicks that hit every channel identically sort nothing, because variation only counts when it differs between competitors (09). The window also survives drift, calculated rather than assumed (derivations D6): drift one power below the noise shifts both edges by the drift-to-noise ratio (1 + a ≤ q ≤ m + 1 + a, and can rescue a system into the window); stronger reinforcement drift replaces noise-dominated sharing with the takeover regime, which is where write-back selection (05) lives; s = q − 1 is the phase boundary between sorting and takeover.

Where does q come from? Not from an assumption. Growth geometry sets it: when throughput rises by recruiting more independently perturbed degrees of freedom (wider contact, more patches, more transactions), throughput and noise variance are extensive in the same units, so D ∝ J and q = m, the window's lower edge, inside for m ≥ 1. When forcing is coherent, amplitudes add before squaring, D ∝ J² and q = 2m, at or beyond the upper edge for m ≥ 1. The two correlation classes of the hidden layer land exactly on the window's two boundaries. This was demonstrated in-substrate with the exponent emerging rather than injected (footprint ∝ share at fixed per-patch coupling: measured 1.01 and 2.00; 09), and with no random number generator anywhere (a deterministic chaotic substrate supplies kicks that are dice to the coarse observer and reproduce to the digit on rerun; 08). One flagged defence still owed for the paper: identify the physically natural variable in which perturbations are additive and unbiased, since a nonlinear change of variables introduces noise-induced drift.

Contact with the world. The exact law is verified by integration and large-N SDE (04: fitted q = 1.00, half-flux fraction matching to four figures). Published exponents place cities (q ≈ 2), GDP (≈ 1.7), firms (≈ 1.5-1.6) and growing networks (≈ 1) inside the window; these are suggestive rather than validating, since observed Var(Δg|g) ∝ g^q can also reflect drift, births and deaths, ageing, nonstationarity, finite windows and measurement noise. The strongest physical case is memristive filaments, where g is genuinely a conductance: measured noise exponents put the diffusive regime far below the window (predicted no sorting; the stable low-resistance state engineers rely on), the ballistic regime inside it (winner-take-all filament formation, as observed), and the broken regime on the upper edge (docs/memristor_q_analysis.md). The caveat is that these are read-noise measurements and the theory wants the state-rewriting rate; the specified parallel-filament array experiment, which can cross both boundaries in one apparatus, is the decisive test.

## 4. Condition 3: establishment is an escape race

A new replicator's offspring inherit its current state, and that state is being pulled home. So reproductive events are correlated through inherited state: the family tends to sink together, and no scalar reproductive number captures the process, however refined. Our instrument runs made this concrete: per-progenitor R₀ up to 30 with zero lineage survival (16, 17b). Survival happens only if some member's state first-passages upward past self-sustaining before the shared decay absorbs the family; copying while rare is multiplied escape attempts, P_surv ≈ 1 − (1 − p_esc)^M. The proper mathematics is a branching diffusion in trait space: with copying rate b(g), death rate d(g), and extinction probability Q(g),

D·Q″ + v·Q′ + b·(Q² − Q) + d·(1 − Q) = 0, P_survive(g) = 1 − Q(g),

one equation holding diffusion, re-templating, inheritance, copying, death and extinction; the escape threshold should emerge from its solution (owed: solve with b = ηJ/E_copy, d from erasure, D from the window, and check against the instrument data). Consequences kept: sparks can be common while establishment is rare (the fizz), failed-chain lengths measure distance to threshold, cycling environments cross it episodically given storage. After escape, takeover is arithmetic, compounding beats accumulation and no further physics is owed; then condition 2 resumes inside the replicator population, evolution proper, with Eigen's mutation window inherited and its free parameter closed by q.

## 5. Condition 4: portability is gated state travelling

The transition marked here is from locally inherited structure (offspring physically continuous with, or reproducing, the parent's structure) to open-ended cumulative heredity: a separable token that can be copied, recombined and expressed in new contexts. Darwinian processes do not require the detached token, so portability is not the definition of life; in plain-language pieces "where life starts" is kept as shorthand for this transition.

The mechanism chain, each link established or named: gating lets a store hold its value without the flow that wrote it (detachability; the riverbed result); gated states are discrete, hence re-instantiable elsewhere, which is what makes a carrier possible; copying-as-refresh economics miniaturise the store toward the minimal gated token, toward a gene; and catalysis reads by configuration rather than position, a catalyst being a configuration-addressed rule. First-pass experiment done (13, 17c): a detached gated token shapes flow 10-60 sites beyond its parent's reach, above a shuffled-token null; the transported self-reinforcing type sweeps the substrate from 0.50 to 0.95; and continuous parcels transmit nothing at any range. Gating is sufficient and necessary here, and the paper-level reason is the transit factor: an ungated parcel's fidelity dies exponentially with distance while a gated one's is near flat (15; derivations D4). Owed: the formal two-variable extension, advected state plus configuration-addressed read, the traveller's extinction equation.

## 6. From sorting to selection: the copying bridge, derived

Sorting becomes selection when state passes between individuals at a rate that rises with share. Previous versions assumed b ∝ J; it is now derived. Let throughput supply usable work at rate ηJ into an accumulator, and let one copy cost E_copy. Then the copy rate is b = ηJ/E_copy, linear in throughput, from two physical conditions only: throughput supplies work, and copying has finite cost. Demonstrated with nothing imposed (18): the linear rate emerges (slope ≈ 0.9 · η/E, the shortfall being daughters starting with empty accumulators), the population mean climbs, the climb scales inversely with copy cost, and the no-copying control stays flat. With inheritance noise supplied by the same hidden layers, variation, heredity and differential reproduction are all present, replicator and Price dynamics apply, and throughput plays two distinct roles from one conserved flow: as contact it makes variation, as work it makes reproduction.

The claim is sized deliberately: these conditions are sufficient for a minimal Darwinian regime within this model class. Both bridges, J → D and J → b, are now testable physical conditions (growth by recruiting independent units; work-funded copying) rather than stochastic assumptions, and each can fail in nameable ways that turn the regime off.

## 7. The worked example: a rainy basin, and where life enters

Take a rainy basin. A fixed amount of water falls each year and must leave by some set of channels: that is the conserved total. Each channel has a state, its width. Wider channels carry more water roughly in proportion: that is the share, Ohm's law for water. Every year each channel's banks are knocked about, silting or scouring. Nothing supplies these knocks from outside: they are the coarse-grained residue of layers the channel description cannot resolve, grain collisions, turbulent gusts, freeze-thaw, animal footfalls, deterministic all the way down and dice at the channel level (P6, demonstrated with no random generator anywhere in sims/core/08). The hidden layers deliver both moments of their influence at once: a fluctuating part, the kicks, undirected, whose size scales with contact and hence with flow (a wider, busier channel touches more churning substrate: variances of independent patches add, sims/core/09); and a mean part, the re-templating pull, the same unresolved physics steadily nudging every channel back toward the width the drive and geometry dictate. Kicks are the mutation; the pull is the forgetting; one source, two moments. How often a channel is kicked, times how hard squared, is its jitter (the diffusivity D); the pull is v; and whether the basin can inherit anything at all is the race between them (condition 1: a dent must outlive the pull long enough to matter).

Two counts. Count channels: over time most are narrow, because a channel that silts up carries little, is rarely disturbed, and stays as it is; the population drifts to where jitter is least. That is Landauer's blowtorch, and all he claimed. Count water: it is carried by the few wide channels, because share follows width and the wide ones, however few, are still wide. Population says trickles; water says a handful of rivers. The counts disagree, and disagree more over time as long as jitter grows at least in proportion to width. Braided rivers and drainage networks are this, measured, with nothing alive in them. The disagreement is the shape Darwin described: many are born, a few carry the future, and the few are not a random sample.

So far no lineage. A wide channel is wide; when it silts it is gone. For the picture to climb rather than spread, width must pass between channels. Rivers do it two ways: a channel wider than its stable size splits, each branch inheriting the parent's cross-section (splitting); a wide channel erodes into a neighbour's catchment and takes its water (capture). Both are copying at a rate rising with share, both are physics, and both make the basin's channels widen on average over time: Price's equation with nothing alive.

What rivers cannot do is carry width as a number. A channel's state travels only with the channel, by splitting or conquest. It cannot be handed to a different channel, stored, varied, and handed on again. That missing row is where the theory says life begins. Grass does it: a tuft drops seed, and the seed carries the root plan without carrying the root. The state has become portable, and once portable it accumulates. The theorem does not need that row; concentration, the disagreement between counts, and the climb by splitting and capture all follow without it. The row is what selection produces when something can carry a state away from its carrier. That is why the same theorem covers rivers and grass, and why it puts the boundary between them at one place: not metabolism, not reproduction, but the point where a channel's state can travel without the channel.

### Term map

| Term | Maths | River basin | Darwin |
|---|---|---|---|
| Conserved total I | fixed sum shared by N channels | the year's rain | carrying capacity, the finite resource |
| Channel i | one of N parts | one channel | one individual or lineage |
| State g | variable setting a channel's share | width | the heritable trait |
| Share g^m/Σg^m | fraction of the total | fraction of water | fitness (once copying is tied to it) |
| Exponent m | how steeply share rises with state | does doubling width double water (yes, m≈1) | how strongly the trait matters |
| Kick | random ± change to g | banks silt or scour | mutation, undirected |
| Kick rate r(g) | how often | more for busier channels | mutation rate, rising with activity (hypothesis) |
| Kick size σ(g) | how big | how much one disturbance changes width | mutation effect size |
| Jitter D = ½rσ² | diffusivity | how much width wanders per year | rate the trait drifts |
| Occupancy p ∝ 1/D | fraction of channels at each state | most channels narrow | the ordinary many (this row is the blowtorch, nothing more) |
| Flux density share·p | fraction of total at each state; flat when q=m | water spread evenly across widths | resource sits in the rare large few |
| Concentration 1 ≤ q ≤ m+1 | vanishing fraction carries finite share | a few channels carry most water | differential success; fails if jitter grows too slowly, or too fast relative to flux |
| Copying ∝ share | a state overwrites a neighbour's | splitting; capture | reproduction; here share becomes fitness by definition |
| Mean trait rises | Δḡ = Cov(g, w)/w̄ (Price) | channels widen on average | descent with modification |
| Write-back c | own flux rewrites own state, sign free | a channel whose flow scours it wider | adaptation; positive sign wins |
| Floor, range | reflecting g_min; spread so far | can't be narrower than zero | extinction; time for diversity |
| Portable state | state carried without its carrier | rivers cannot; seed can | heredity as such; where life starts |

*Free premises, not in the theorem:* kick rate (more precisely D) rises at least linearly with state; share is linear in state; copying goes with share. Each is a claim about the world to be measured.

*The equation.* p(g) ∝ 1/D(g). With share ∝ g^m and D ∝ g^q: flux density ∝ g^(m−q); concentration iff 1 ≤ q ≤ m+1, both edges marginal; the toy is q = m, inside the window for all m ≥ 1.

## 8. The heredity ladder (the physical realisation)

Rung 0, open flow: gradient re-templates everything; weather; heredity is rare in flows and must be earned. Rung 1, closed loop: heredity-in-time via the momentum term; one lineage; type-memory only. Rung 2, bifurcation: heredity across lineages iff the daughter's state is caused by the parent's state, not the environment (shedding is production, not replication; channel splitting and the turbulent cascade are replication at low fidelity); measured in the carved bed, excess +0.21 over the matched null at zero healing, gone by λ = 0.05 (sims/core/10); REFRAMED by the stricter null (17a): the signal is carved-line continuity, so at bifurcation inheritance and connectivity are one mechanism; detached transmission is rung 3's, shown there. Rung 3, externalised gated state: the record outlives the revolution, then the carrier; condition 4's territory.

## 9. Definitions

- D1. *Pattern*: a configuration distinguishable from background at some resolution.
- D2. *Gradient-rebuilt* vs *self-rebuilt* pattern: re-formed each instant from ambient physics, versus re-formed by reference to its own prior state. Both are flow; both replace their substance. The rebuild rule is the difference. Whirlpool: nudge it, the gradient restores the old shape. DNA: nudge a base, the next copy carries the nudge. Refined below.
- D2a. The heredity ladder, four rungs. (0) Open flow: no memory; the gradient re-templates every disturbance (weather; most flows; heredity is rare in flows and must be earned, not assumed). (1) Closed loop: heredity-in-time; each turnover templated by the previous one via the momentum term; one lineage, generations = turnovers, fidelity < 1 (the whirlpool, dying and reborn each cycle). (2) Bifurcation: heredity across lineages, iff the daughter's state is caused by the parent's state rather than by the environment. Vortex shedding is production, not replication (the obstacle templates each vortex); channel splitting and the turbulent cascade (eddies begetting eddies) are replication at low fidelity. (3) Externalised state: state moves into a slower substrate the flow reads and writes (bump, catalyst bed, DNA); fidelity decouples from the flow's turnover; the record outlives the revolution, then the carrier.
- D2b. The templating (sticking) condition: heredity survives at any rung exactly when the pattern's own state outcompetes the gradient as template for the next state. Twin of D6: self-routing is how much of your sustaining flux is your own doing; self-templating is how much of your successor's state is. Heredity emerges where self-templating crosses threshold: a measurable transition, not an added ingredient.
- Terminology ruling: pre-copying, the theorems deliver *sorting* (differential persistence, Vrba-Gould), not selection. Write-ups must say sorting until the copying bridge is explicitly in place.
- D3. Domain: gradient-rebuilt patterns and the self-rebuilt patterns they couple to. Kinetically trapped order (crystal, table) is outside: its entropy bill was paid once at creation; ours is paid continuously because existence and rebuilding are the same event.
- D4. *Loop in flow*: closed circulation distinct from through-flux. Needs two spatial dimensions (a 1D world has no interior), a conserved current (Life has none, so its gliders are travelling wobbles), and a nonlinearity (linear flow cannot tell upstream from down). A spiral is a circle plus a through-flux: closed in one direction (boundary, identity), open in the other (metabolism). A wobble repeats in time but encloses nothing: it leaks; a loop traps.
- D5. A pattern is *real* at a resolution if its shorthand predicts as well as tracking the parts (predictive closure); its *boundary* is the contour where the shorthand stops leaking. Not yet operational on a lattice.
- D6. *Self-routing ratio*: fraction of a pattern's sustaining flux that would not exist without it. Shaping loops (near 0: whirlpool, the water came anyway) vs causing loops (near 1: fire, no fire no oxidation). Independent of intensity. No agency implied; causal topology only.
- D7. *Hybrid*: a gradient-rebuilt loop coupled to a self-rebuilt pattern it reads and writes. Rule and flow are one substrate at two speeds; the channel between them is what a timescale separation is.
- D8. *Rule*: a local input-to-output mapping; misapplication under noise is a kink.
- D9. *Loop in memory*: rule shapes flow, flow writes rule, written rule shapes next flow. Same object as D4, one level up.

## 10. Rules (the objects selection acts on)

- R1. A rule is a standing local property that shapes how flow passes a point, is not consumed by that flow, and can differ from point to point. In the toy, g. In chemistry, a catalyst. In a CA, the update law if allowed to be local.
- R2. A catalyst is a rule. Which catalyst is present determines how the flow runs, without symbols. DNA is a catalyst set stored one level up. The gap is capacity, not kind.
- R3. A rule becomes heritable when it is local, stored in state, and carried and re-instantiated by the patterns it steers. Rule 110 fails all three: global, external, uncarried. That is why it computes and never evolves.
- R4. Misapplication under noise is a kink, the minimal nonlinearity. Where flux is, misapplication is more frequent (P6a).
- R5. Two rules in the toy: g (how much flux the channel passes; the phenotype the flow sees) and c (how the channel's throughput rewrites g; a rule about the rule; the genotype of the memory loop). Both kicked, both copied.
- R6. Rule and flow are one substrate on two timescales. Sand is the rule, erosion is the write; nobody supplies a channel. The "reading problem" was an artefact of drawing rule and flux as separate variables.
- R7. The evolving rule is not the physics rule. Ohm splitting, kick ∝ share, copy ∝ share, fixed total: universal and unvaried. Selection happens by them, not on them.

## 11. Premises

- P1 (First law): energy conserved.
- P2 (Second law): local order paid for with disorder elsewhere, at the time of the transaction.
- P3 (Minimum price, restricted): stated as a lemma, L1 below. No general floor for order merely existing.
- P4 (Instability): above critical throughput smooth relaxation is impossible; structure forced. Proven for convection; reproduced in our lattice; nonlinearity shown necessary.
- P5 (Preferred scale): flow structures have a stable size; surplus makes more, not bigger. Empirical; not reproduced by us.
- P6 (Noise): whatever an observer cannot resolve appears as irreducible noise in what they can (Mori-Zwanzig). Hidden below, dice above. *Demonstrated in-substrate:* a deterministic chaotic layer under the channels produces kicks that are dice to the coarse observer, with variance scaling as share² from contact alone, and concentration follows with no RNG anywhere (sims/core/08). Caveat learned there: selection needs activity-scaled variance, not unpredictability; a periodic substrate concentrates too. Mutation means blind and scaled, not uncaused.
- P6a, resolved into a classification (demonstrated in-substrate, sims/core/09): how D scales with J is set by how a channel grows. *Extensive* growth (throughput adds independent units: patches, transactions, members) gives kick variances that add, so D ∝ J, q = m, inside the window; measured emergent exponent 1.01 with footprint ∝ share at fixed per-patch coupling on a chaotic substrate. *Intensive/coherent* growth (same units, bigger amplitude, or one shared environmental signal) gives D ∝ J², q = 2m ≥ m+1, at or beyond the upper edge; measured 2.00. The exponent is not a free parameter; it is the geometry of growth, measurable per system. Additional finding: common-mode noise (perfectly correlated across channels) fails to select even at nominally in-window q, because selection requires noise that differentiates competitors; variation must be idiosyncratic. Original statement kept for history:
- P6a (original form, superseded above): the diffusivity of a channel's state in the privileged variable g scales as g^m, i.e. with its throughput. Equilibrium FDT does not give this; far from equilibrium FDT is generically violated (Harada-Sasa). Status: hypothesis to be derived or tested per system class. Evidence in the direction: transcription-associated mutagenesis; metabolic-rate scaling of molecular evolution. Also assumed: kicks additive and symmetric in g (the stochastic metric); reparameterization changes the apparent exponent.
- P6b (Transport): what a flow can move, it moves in proportion to itself.
- P7 (Finitude): every gradient is finite.
- P8 (Storage): configurations stable between copies can hold information (Schrödinger's aperiodic crystal); their role is stability between copies, not permanence.
- P9 (Description/constructor): cumulative replication needs a stored description plus a reader (von Neumann).
- P10 (Linear response): share of flux rises at least linearly with the state that carries it, m ≥ 1. Ohm, stream power, catalysis satisfy; diffusion alone does not.

## 11a. Lemma L1 (irreversible maintenance)

In the domain of D3 a pattern persists only by being rebuilt. Rebuilding against noise means the noised state is discarded and the pattern's state re-imposed; discarding a state is logically irreversible, hence carries the Landauer erasure cost per erased degree of freedom per rebuild. Therefore maintained order in this domain has a minimum dissipation rate proportional to (order held) × (rebuild rate). Landauer supplies the cost of erasure; the lemma supplies the claim that maintenance contains erasure. The second half is what must be checked per system, not assumed. Outside D3 (kinetically trapped order) the lemma does not apply and no floor is claimed.

## 12. Entropy: where it enters and where it does not

- The headline: entropy is produced when order degrades, not when it is created. Creation defers (production below the bare-gradient ceiling while order is banked); maintenance holds at the ceiling; degradation repays; the full cycle closes at the bare total. Structure is a timing device for entropy production.
- The resolving fact: everything ordered on Earth is higher entropy per joule than the sunlight that paid for it (5800 K light ~0.0002 J/K per joule; 300 K chemistry ~0.003). Order here is a rung down the ladder from sun to space, not a climb back up.
- A heat engine at fixed heat flow cannot increase total entropy production; the bare gradient is the ceiling. Structure acts on inputs and routes (albedo, unlocking, interception: the one door, and the ratchet), never on entropy per joule of output. A mill is a structured flow; it can dam the stream, not lower the sea.
- Hence the currency of competition is share of flux; dissipation is the bill, identical for all arrangements per captured joule over a full cycle. Full ledger, three Earths, fossil/Dyson objections: docs/entropy_ledger.md.
- Selection is Lotka's 1922 conjecture given a mechanism and a window: within the window, channels holding a larger share of the free-energy flux, and able to maintain themselves on it, persist and spread. A bias, not a maximisation.

## 13. Derivation chain (T-claims)

- T1 (existing is paying). From D2 + P2 + P3: a flow pattern exists only while paying; existing and being rebuilt are one event.
- T2 (the ceiling). From T1 + P7: for a given flux, a maximum maintained negentropy. Well supported for erasure-maintained patterns; not a general theorem.
- T3 (the corridor). From P4 + T2: below threshold no pattern holds; above it, patternlessness cannot hold.
- T4 (loops are things). From D4 + D5: identity in the pattern, boundary non-arbitrary. Ship of Theseus resolved: identity lives in the loop.
- T5 (loops self-route to varying degrees, and capture). From D6.
- T6 (competition). From T2 + P5 (or copying) + P7: multiplication of fixed-intake loops alone exhausts a finite gradient. Growth (causing loops expanding at their edge) and capture add to this but are not required.
- T7 (multiplication). From P5, or from copying (iv).
- T8 (variation): rebuilding under noise guarantees it; erased in gradient-rebuilt patterns, carried in self-rebuilt.
- T8a (memory alone needs a gate): a plain relaxation-to-self only slows forgetting; persistence needs a threshold. When the write goes through the flow, the loop is its own nonlinearity and no gate is needed.
- T9 (selection): concentration and differential persistence from Theorem (i)–(iii), inside the window 1 ≤ q ≤ m+1; Darwinian selection only once copying ∝ share is added (iv), which is the bridge; reflexivity from (v).
- T10 (robust win, prediction): persisting types are noise-robust, multiply realizable.
- T10a (stasis without memory): flow alone yields a stable zoo of types, not lineages. Bénard rolls forever is this theorem.
- T11 (memory migrates to self-rebuilt patterns): only there does variation outlive one rebuild. DNA is not durable stuff; it is a flow whose maintenance step is a copy.
- T12 (the hybrid is the unit of evolution): a loop that lives, carrying a self-rebuilt pattern that is read and copied at partition under noise.
- T12a (reading is selected, not installed): any flow-to-rule channel with free sign is closed into a loop by selection.
- T13 (selection does not stop, but not by one trait): on a single scalar trait selection is self-extinguishing (at the ceiling every survivor carries a near-equal share and the flux stops distinguishing). It continues because: at the ceiling P5 forces splitting, turning competition zero-sum; causing loops that unlock held-back gradient raise the total flux and with it the ceiling (complexity ratchets by capture, bounded at each moment by T2); and the environment is the other channels, so the share landscape co-evolves and never flattens.

## 14. Darwin map

See the term map in §1. Additions not in the table: death = freezing at the floor or being overwritten; drift = the flat-noise control; genotype/phenotype = c/g in the write-back toy, self-rebuilt pattern / flow loop in the hybrid, reading is the map between them; environment = the other channels plus the fixed total. Missing from the toy: recombination; an error threshold (a single number cannot be corrupted).

## 15. Status and open items

Sims: eighteen core experiments and five boundary studies, each with an honest status in `docs/experiments.md`; downgrades and reframes forced by our own controls are kept in the record (the near-tautological consistency check, the continuity reframe of rung 2, the correlated-fates failure of scalar R₀, the confounded first ungated control and its clean redesign).

Pencil, in priority order: solve the branching-diffusion extinction equation against the instrument data; hand-check the derivation sketches in `docs/derivations.md` (Kramers dent-life with its scope condition; the accumulator; invasion against incumbents; the portability transit factor); state the additive-variable defence (D0) for the paper.

Contact with the world: one system with J, r and σ² measured together (the memristor parallel-filament array is specified and decisive, crossing both window boundaries in one apparatus); any biological q; the firms transient-versus-stationary exponent followed over time.

Unexplained and owned as such: P5, why surplus makes more rather than bigger, the splitting primitive; D5's predictive-closure boundary not yet operational on a lattice.

Papers: paper 1 per the spec in `docs/papers.md`, ruthlessly narrow, no entropy, ending at the derived Darwinian regime and the two-sided m = 1 prediction whose counterintuitive upper boundary is the headline. The entropy ledger and the grand synthesis follow it, not precede it.

## Repository

- `docs/results_one_liners.md`: each experiment in one sentence with its figure.
- `docs/experiments.md`: what was run, what it showed, which script and figure.
- `docs/derivations.md`: the four derivations, sketch rigour, assumptions flagged, two new predictions.
- `docs/memristor_q_analysis.md`: q computed from measured memristor noise exponents; one physical system crosses the window.
- `docs/entropy_ledger.md`: the sun–Earth–space entropy ledger; three Earths (dirt, diamond, whirlpool).
- `docs/references.md`: prior art to cite and the literature check.
- `docs/papers.md`: the paper plan.
- `docs/history.md`: ΛB post-mortem and distinctions kept from the working conversation.
- `docs/substack_draft.md`: plain-English essay.
- `docs/animation_brief.md`: build brief for a one-world explainer animation (illustration, not evidence).
- `sims/core/`: the theorem and its checks (paper 1). `sims/boundaries/`: what linear systems cannot do (paper 2). Numbered in the order of the argument.
- `figures/core/`, `figures/boundaries/`: one figure per result, named for what it shows.
