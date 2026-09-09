# Conserved-flow validation results

Python 3.12.14; NumPy 2.3.5.

N=8; state interval [1,3]; 8 grid intervals; 128 independent ensembles per seed; 3 seeds; final physical time 16.

Six exponent pairs; four initial conditions, including both boundaries. Snapshots are taken at fixed physical times. Final errors pool seeds, not observation times. The snapshot reference uses 100,000 independent samples of the exact joint law.

Acceptance: every final absolute error below 0.05. Result: PASS.

| Observable | Largest final error |
|---|---:|
| occupancy_cdf_error | 0.020299 |
| flow_cdf_error | 0.024502 |
| snapshot_half_error | 0.005979 |

These finite-grid checks do not establish convergence at arbitrary state ranges. Grid refinement compares the exact grid stationary law with the continuum expression; it is separate from the dynamical check. No time-step approximation is used by the event simulator.
