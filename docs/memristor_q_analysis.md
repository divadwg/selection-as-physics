# A physical system on the window: q from measured memristor noise

Source: Balogh, Mezei, Pósa, Sánta, Magyarkuti, Halbritter, "1/f noise spectroscopy and noise tailoring of nanoelectronic devices" (arXiv:2106.02683), reporting Ag₂S filament measurements (Sánta et al., Nanoscale 2019) and Ta₂O₅/Nb₂O₅ (Sánta et al., ACS AMI 2021). All free.

## Translation
State g = filament conductance G. Share at fixed voltage ∝ G, so m = 1. Measured: relative fluctuation ΔG/G vs resistance (ΔI/I = ΔG/G in the linear regime). Spectra are 1/f-type (γ ≈ 1.12), so the low-frequency state-noise power, our effective diffusivity D, scales as (ΔG)².

## Measured exponents → q
| Regime | Measured | ΔG scaling | D ∝ (ΔG)² | q | vs window (m = 1: 1 ≤ q ≤ 2) |
|---|---|---|---|---|---|
| Diffusive (wide metallic filament, low R) | ΔG/G ∝ G^(−3/2) | G^(−1/2) | G^(−1) | ≈ −1 | far below: NO selection predicted |
| Ballistic (atomic filament) | ΔG/G ∝ G^(−1/4) | G^(3/4) | G^(3/2) | ≈ 1.5 | inside: selection predicted |
| Broken (tunnelling) | ΔG/G ≈ const | G | G² | ≈ 2 | exactly the upper marginal edge |

## Predictions vs known phenomenology
- Below the window (diffusive): no concentration, and p ∝ g^(+1): population biased toward high-G. Known: the low-resistance state is the stable, retentive one; relative noise collapses as filaments widen. The "well-damped high-throughput channel" falsifier regime exists and behaves as predicted.
- Inside the window (ballistic): concentration. Known: atomic-scale filament formation is winner-take-all; one filament takes the current.
- Upper edge (broken): marginal.

## Caveats (all real)
- These are steady-state read-noise measurements at low bias; the theory's D is state-rewriting jitter under drive. Identifying them assumes the same fluctuators move the state (stimulated ionic telegraph noise, Sci Rep 2019, supports this qualitatively).
- Single devices tuned across states, not a population sharing a fixed current: the conservation/census half of the theorem is untested by this data.
- "Winner-take-all" is known qualitatively, not measured as a share distribution over time.
- Exponents come via a point-contact transport model fitted to the data.

## The finishing experiment (precisely specified)
An array of filaments sharing one current source; track the share distribution over time; run once with wide diffusive filaments (predict: no concentration) and once at atomic/ballistic scale (predict: concentration). Same apparatus as the cited work.

Figure: figures/core/memristor_regimes_cross_the_window.png
