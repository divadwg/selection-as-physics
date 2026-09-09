"""Structural checks independent of the simulation's reported fit."""
import itertools
import importlib.util
from pathlib import Path
import unittest
import numpy as np
from sims.validation.conserved_flow import (
    Model, stationary_marginals, exact_samples, observables, simulate,
    continuum_half, pooled_half,
)


class ConservedFlowTests(unittest.TestCase):
    def test_joint_detailed_balance_and_marginal_by_enumeration(self):
        # Enumerate the full configuration space, rather than assuming the
        # marginal formula or relying on a fitted histogram.
        for m, q in [(1, 0.5), (1, 1), (1, 2.5), (2, 4)]:
            model = Model(n=3, m=m, q=q, upper=3, intervals=2)
            states = np.array(list(itertools.product(range(3), repeat=3)))
            g = model.grid[states]
            s = (g**m).sum(axis=1)
            joint = s * np.prod(g**(-q), axis=1)
            joint /= joint.sum()
            lookup = {tuple(x): i for i, x in enumerate(states)}
            for index, state in enumerate(states):
                for channel in range(model.n):
                    if state[channel] == model.intervals:
                        continue
                    neighbour = state.copy()
                    neighbour[channel] += 1
                    j = lookup[tuple(neighbour)]
                    forward = model.n * g[index, channel]**q / s[index] / model.spacing**2
                    backward = model.n * g[j, channel]**q / s[j] / model.spacing**2
                    self.assertAlmostEqual(joint[index] * forward, joint[j] * backward, places=12)
            actual_p = np.bincount(states[:, 0], weights=joint, minlength=3)
            actual_f = np.bincount(states[:, 0], weights=model.n*joint*g[:, 0]**m/s, minlength=3)
            _, p, f = stationary_marginals(model)
            np.testing.assert_allclose(actual_p, p, atol=1e-14)
            np.testing.assert_allclose(actual_f, f, atol=1e-14)

    def test_single_channel_share_is_one(self):
        model = Model(n=1, m=1, q=1)
        _, p, f = stationary_marginals(model)
        np.testing.assert_allclose(p, np.full(len(p), 1/len(p)))
        np.testing.assert_allclose(p, f)
        samples = exact_samples(model, 100, np.random.default_rng(3))
        self.assertEqual(observables(model, samples)[2], 1.0)

    def test_finite_population_quantile_identity(self):
        for n in [1, 8, 40]:
            for q in [0.5, 1, 2, 2.5]:
                model = Model(n=n, q=q, intervals=128)
                base, p, f = stationary_marginals(model)
                self.assertAlmostEqual(pooled_half(p, f), (1-1/n)*pooled_half(base, f)+0.5/n)

    def test_exact_joint_sampling(self):
        model = Model(n=8, q=2.5)
        samples = exact_samples(model, 30000, np.random.default_rng(3))
        p, f, _ = observables(model, samples)
        _, expected_p, expected_f = stationary_marginals(model)
        np.testing.assert_allclose(p, expected_p, atol=0.006)
        np.testing.assert_allclose(f, expected_f, atol=0.006)

    def test_exact_half_fraction_and_margins(self):
        for r in [100, 1e4, 1e8]:
            self.assertAlmostEqual(continuum_half(1, 2, r), 1/(np.sqrt(r)+1), places=12)
            self.assertAlmostEqual(continuum_half(1, 1, r), np.log(2*r/(r+1))/np.log(r), places=12)
        self.assertAlmostEqual(continuum_half(1, 2.5, 1e12), 0.125, places=5)

    def test_analytic_quantiles_against_original_numerical_integral(self):
        path = Path(__file__).resolve().parents[1] / "sims/core/04_selection_window_exact_law.py"
        spec = importlib.util.spec_from_file_location("original_integral", path)
        original = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(original)
        for m, q in [(1,.5), (1,1), (1,1.5), (1,2), (1,2.5), (2,4)]:
            for upper in [100, 1e4, 1e8]:
                self.assertAlmostEqual(continuum_half(m,q,upper), original.P_half(m,q,upper), delta=1e-4)

    def test_grid_refinement(self):
        target = continuum_half(1, 1, 3)
        errors = []
        for intervals in [8, 32, 128]:
            model = Model(q=1, intervals=intervals)
            base, _, flow = stationary_marginals(model)
            errors.append(abs(pooled_half(base, flow)-target))
        self.assertLess(errors[1], errors[0])
        self.assertLess(errors[2], errors[1])

    def test_physical_time_simulation_from_both_extremes(self):
        # q=m with one channel gives a simple symmetric reflecting walk.
        # This catches biased jump sampling and asymmetric boundary handling.
        model = Model(n=1, m=1, q=1, intervals=2)
        for initial in ["low", "high"]:
            last = simulate(model, 5000, [0, 10], initial, 7)[-1]
            p, f, half = observables(model, last)
            np.testing.assert_allclose(p, np.full(3, 1/3), atol=0.025)
            np.testing.assert_allclose(p, f)
            self.assertEqual(half, 1.0)


if __name__ == "__main__":
    unittest.main()
