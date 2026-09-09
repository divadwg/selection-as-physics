"""
HISTORICAL SUMMARY ONLY: no runnable implementation of these follow-ups is
present in this file. Numbers below have not been reproduced in the current
audit. Claims ruling out all R0 descriptions or proving gating necessary are
withdrawn; see docs/heredity_audit.md and sims/validation/heredity.py.

Three follow-ups reported 2026-08-22 (methods and numbers; see docs/experiments.md for the record):
1. Stricter same-drainage null on h2 (junction pairs vs straight-segment pairs, lam=0):
   junction +0.40±0.18, straight +0.66±0.07. The h2 signal is carved-line CONTINUITY, not
   branching-specific transmission; at bifurcation in this system inheritance = connectivity.
2. R0 instrument v2 (trajectory-integrated R0_eff along the decaying trait path):
   R0_eff up to 30 with P_surv = 0; survival only at ktemp=5e-4 (P=0.13). Establishment is NOT
   an R0 phenomenon here at any refinement: it is a first-passage ESCAPE race (some member's g
   must random-walk past self-sustaining before the family's shared decay absorbs it).
   P_surv ≈ 1 - (1 - p_esc)^M. Two-stage law: escape first, compounding after.
3. Ungated-necessity control (rung-3 world, no types in ungated mode; parcel carries blurred
   continuous g): gated effect +1.52 (near, d 10-35) and +1.25 (far, d 35-80), flat; ungated
   +0.04 / +0.01, nothing at any range. Gating necessary and sufficient for portability here.
Code for all three is preserved in the conversation record; this file is the citable summary.
"""
