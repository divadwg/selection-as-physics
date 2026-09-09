"""Run with python -m sims.validation.run_validation --output DIRECTORY."""
import argparse
import csv
from pathlib import Path
import platform
import numpy as np
from .conserved_flow import (
    Model, stationary_marginals, exact_samples, observables, simulate,
    continuum_half, pooled_half,
)


def write_csv(path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("docs/validation_results"))
    parser.add_argument("--replicas", type=int, default=128, help="Independent ensembles per seed")
    parser.add_argument("--seeds", type=int, default=3)
    parser.add_argument("--intervals", type=int, default=4)
    parser.add_argument("--channels", type=int, default=8)
    parser.add_argument("--upper", type=float, default=3.0)
    parser.add_argument("--horizon", type=float, default=16.0)
    args = parser.parse_args()
    if args.replicas < 1 or args.seeds < 1 or args.horizon <= 0:
        parser.error("replicas, seeds and horizon must be positive")
    args.output.mkdir(parents=True, exist_ok=True)
    cases = [(1, 0.5), (1, 1), (1, 1.5), (1, 2), (1, 2.5), (2, 4)]
    initials = ["low", "high", "log_uniform", "stationary"]
    times = [0, args.horizon/16, args.horizon/4, args.horizon]
    rows, final_rows = [], []
    for case, (m, q) in enumerate(cases):
        model = Model(n=args.channels, m=m, q=q, upper=args.upper, intervals=args.intervals)
        _, expected_p, expected_f = stationary_marginals(model)
        reference = exact_samples(model, 100000, np.random.default_rng(90000+case))
        reference_half = observables(model, reference)[2]
        for initial_index, initial in enumerate(initials):
            final_states = []
            for seed in range(args.seeds):
                actual_seed = 10000*case+1000*initial_index+seed
                snapshots = simulate(model, args.replicas, times, initial, actual_seed)
                final_states.append(snapshots[-1])
                for t, states in zip(times, snapshots):
                    p, f, half = observables(model, states)
                    rows.append(dict(m=m, q=q, initial=initial, seed=actual_seed, time=t,
                                     occupancy_cdf_error=float(np.max(abs(np.cumsum(p-expected_p)))),
                                     flow_cdf_error=float(np.max(abs(np.cumsum(f-expected_f)))),
                                     snapshot_half=half, reference_snapshot_half=reference_half))
            p, f, half = observables(model, np.concatenate(final_states))
            row = dict(m=m, q=q, initial=initial,
                       occupancy_cdf_error=float(np.max(abs(np.cumsum(p-expected_p)))),
                       flow_cdf_error=float(np.max(abs(np.cumsum(f-expected_f)))),
                       snapshot_half_error=abs(half-reference_half))
            final_rows.append(row)
            print(f"m={m:g} q={q:g} {initial:11s} occupancy={row['occupancy_cdf_error']:.4f} "
                  f"flow={row['flow_cdf_error']:.4f} snapshot={row['snapshot_half_error']:.4f}", flush=True)
    write_csv(args.output/"dynamics.csv", rows)
    write_csv(args.output/"final_errors.csv", final_rows)
    grids = []
    for m, q in cases:
        for intervals in [4, 8, 16, 32, 64, 128, 256]:
            model = Model(n=args.channels, m=m, q=q, upper=args.upper, intervals=intervals)
            _, p, f = stationary_marginals(model)
            exact = (1-1/model.n)*continuum_half(m,q,model.upper)+0.5/model.n
            grids.append(dict(m=m,q=q,intervals=intervals,grid_pooled_half=pooled_half(p,f),
                              continuum_pooled_half=exact,error=abs(pooled_half(p,f)-exact)))
    write_csv(args.output/"grid_refinement.csv", grids)
    limits = []
    for q in [0.5, 1, 1.5, 2, 2.5]:
        for upper in [1e2, 1e4, 1e6, 1e8]:
            base = continuum_half(1,q,upper)
            for n in [8,40,400,4000]:
                limits.append(dict(m=1,q=q,upper=upper,n=n,base_half=base,
                                   conserved_pooled_half=(1-1/n)*base+0.5/n))
    write_csv(args.output/"population_limits.csv", limits)
    # A declared numerical acceptance criterion, not a statistical confidence
    # interval or a theorem. Per-seed data and initial transients remain in CSV.
    tolerance = 0.05
    passed = all(max(r["occupancy_cdf_error"], r["flow_cdf_error"],
                     r["snapshot_half_error"]) < tolerance for r in final_rows)
    maximum = {name:max(r[name] for r in final_rows) for name in
               ["occupancy_cdf_error","flow_cdf_error","snapshot_half_error"]}
    report = ["# Conserved-flow validation results", "",
              f"Python {platform.python_version()}; NumPy {np.__version__}.", "",
              f"N={args.channels}; state interval [1,{args.upper:g}]; {args.intervals} grid intervals; "
              f"{args.replicas} independent ensembles per seed; {args.seeds} seeds; "
              f"final physical time {args.horizon:g}.", "",
              "Six exponent pairs; four initial conditions, including both boundaries. "
              "Snapshots are taken at fixed physical times. Final errors pool seeds, "
              "not observation times. The snapshot reference uses 100,000 independent "
              "samples of the exact joint law.", "",
              f"Acceptance: every final absolute error below {tolerance}. "
              f"Result: {'PASS' if passed else 'FAIL'}.", "",
              "| Observable | Largest final error |", "|---|---:|"]
    report += [f"| {name} | {value:.6f} |" for name,value in maximum.items()]
    report += ["", "These finite-grid checks do not establish convergence at arbitrary "
               "state ranges. Grid refinement compares the exact grid stationary law "
               "with the continuum expression; it is separate from the dynamical check. "
               "No time-step approximation is used by the event simulator.", ""]
    (args.output/"README.md").write_text("\n".join(report))
    if not passed:
        raise SystemExit("Validation criterion failed; inspect transients and increase sampling or equilibration as justified")


if __name__ == "__main__":
    main()
