# References and literature check

## Current paper: scope of the literature comparison

The [revised paper](../paper/README.md) treats the upper edge as a standard
weighted-moment threshold applied to a specified coupled flow model. This is not
a claim to have discovered the underlying integrability condition. A targeted
literature check does not establish priority for the exact model either.

- [Landauer (1988), Motion out of noisy states](https://doi.org/10.1007/BF01011555),
  and [Maes and Netočný (2013)](https://arxiv.org/abs/1207.1122): established work
  on state-dependent kinetics and occupations.
- [Newman (2005)](https://arxiv.org/abs/cond-mat/0412004): power-law moments (Section III.B) and
  concentration of weighted quantities (Section III.D). This is essential context for the upper
  threshold, rather than an unrelated comparison.
- [Clauset, Shalizi and Newman (2009)](https://arxiv.org/abs/0706.1062): methods and
  limitations of empirical power-law inference.
- [Krapivsky, Redner and Leyvraz (2000)](https://arxiv.org/abs/cond-mat/0005139):
  nonlinear attachment in growing networks. Its linear boundary is not the same
  theorem as the lower noise boundary here.
- [Bouchaud and Mézard (2000)](https://arxiv.org/abs/cond-mat/0002374): wealth
  exchange and multiplicative noise. Different dynamics and a different
  concentration observable.

The exact coupled calculation and finite-population correction are results
presented in this repository. Their derivation is explicit; whether equivalent
formulations already exist requires a more exhaustive literature comparison.

## Deterministic dynamics and effective noise

[Melbourne and Stuart (2011, corrected 2015)](https://arxiv.org/abs/1101.3087)
derive stochastic diffusion limits from deterministic fast-slow systems.
[Gottwald and Melbourne (2013, corrected 2015)](https://arxiv.org/abs/1304.6222)
show why multiplicative deterministic forcing requires care over effective drift
and stochastic interpretation. These establish relevant ingredients; they do
not establish the combined flow-window-to-selection mechanism proposed here.
The repository's particular lattice has not yet been shown to satisfy a
corresponding diffusion-limit theorem.

## Historical research notes

The notes below are retained for provenance. Statements such as “not found” do
not establish novelty; identifications with preferential attachment and broad
physical or evolutionary claims should not be treated as conclusions of the
current paper.


Prior art: Landauer 1975 (blowtorch; also kills minimum-entropy-production); Landauer J. Stat. Phys. 1975; Maes & Netočný 2012 (Ann. Henri Poincaré, arXiv 1207.1122); Maes 2020 Phys. Rep. 850 (frenesy); Basu & Maes (frenesy and response); Bergin & Lipman 1996 Econometrica (state-dependent mutation rates select arbitrarily); van Damme & Weibull (mutations driven by control costs); Sawa 2011; Krapivsky, Redner & Leyvraz 2000; Jeong, Néda & Barabási 2003 (γ ≈ 1 measured); Eigen & Schuster (hypercycles); Fisher; Moran; Price; England (dissipative adaptation, distinguish); Kauffman; Park, Qian & Zhang 2012 (transcription-associated mutagenesis); Gillooly & Allen (metabolic rate and molecular evolution); Maynard Smith (limited vs unlimited heredity); Schrödinger; von Neumann; Crutchfield & Hanson (computational mechanics); Mori-Zwanzig.



Also: Lotka 1922 (natural selection increases energy flux; the 'maximum power' lineage via H.T. Odum). Our theorem is a mechanism and a boundary for Lotka's conjecture: within the window, channels holding a larger share of free-energy flux, and able to maintain themselves on it, persist and spread. Not maximisation; a bias, conditional on the window and on flux still separating channels.

## Literature check (status)

Landauer 1975 and Maes-Netočný 2012 supply the occupancy mechanism (least frenetic states dominate). Bergin-Lipman 1996 and successors show state-dependent mutation rates can select arbitrarily; our claim is that a physical hypothesis on D(g) removes the arbitrariness. Krapivsky-Redner-Leyvraz 2000 give the sublinear/linear/superlinear regimes of preferential attachment; the lower edge of our window is that boundary and must be cited. Not found: the population/flux inversion under a conserved total; the two-sided window 1 ≤ q ≤ m+1; the physical placement q = m; copying and write-back on such a substrate. Frenesy papers steer currents by activity set externally, not self-generated. Reads owed: Bergin-Lipman in full; Landauer's later essays; Eigen-Schuster; England.
