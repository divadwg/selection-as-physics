"""Check whether fine-lattice variation differentiates initially identical routes.

This reuses experiment 08 with initial_spread=0. The fine initial state remains
heterogeneous; all subsequent updates are deterministic. It tests route
differentiation, not formation of a spatial network or the full noise window.
"""
import csv
import hashlib
import importlib.util
from pathlib import Path
import platform
import warnings

import numpy as np


def main():
    root = Path(__file__).resolve().parents[2]
    source = Path(__file__).with_name("08_mutation_from_unseen_layers_no_rng.py")
    spec = importlib.util.spec_from_file_location("lattice_routes", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    target = root / "docs/research_examples/equal_route_start.csv"
    with target.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "mode", "seed", "channels", "steps", "initial_spread", "initial_top3",
            "final_top3", "variance_slope", "gray_autocorrelation",
        ], lineterminator="\n")
        writer.writeheader()
        for seed in [0, 1, 2]:
            for mode in ["chaotic", "frozen"]:
                # The frozen control has zero variance; its correlation is undefined.
                with warnings.catch_warnings():
                    warnings.filterwarnings("ignore", message="invalid value encountered in divide", category=RuntimeWarning)
                    result = module.run(mode=mode, seed=seed, initial_spread=0.0)
                if mode == "frozen" and not np.isclose(result["top3"], 3/40, atol=1e-14):
                    raise AssertionError("Frozen equal routes did not preserve equal shares")
                writer.writerow(dict(
                    mode=mode, seed=seed, channels=40, steps=60000,
                    initial_spread=0.0, initial_top3=3/40,
                    final_top3=result["top3"], variance_slope=result["kickvar_vs_share_slope"],
                    gray_autocorrelation=result["gray_autocorr"],
                ))
                handle.flush()
                print(f"{mode}, seed {seed}: top-three share {3/40:.3f} -> {result['top3']:.6f}", flush=True)
    target.with_suffix(".txt").write_text(
        "Equal coarse-route initialization; fine-lattice initialization unchanged.\n"
        "All other parameters are experiment 08 defaults.\n"
        f"Python {platform.python_version()}; NumPy {np.__version__}\n"
        f"Source SHA256: {hashlib.sha256(source.read_bytes()).hexdigest()}\n"
        f"Runner SHA256: {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}\n"
        "Frozen correlations and variance slopes are undefined (nan).\n"
    )


if __name__ == "__main__":
    main()
