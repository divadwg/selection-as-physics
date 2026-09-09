"""Independent analytic controls for lineage and carrier calculations."""
import unittest
import numpy as np
from sims.validation.heredity import Branching, transmit, generations, trait_model


class HeredityTests(unittest.TestCase):
    def test_birth_death_against_closed_form(self):
        for birth in [.2, .4, .8]:
            death = .4
            model = Branching(np.zeros((1,1)), np.array([birth]), np.array([death]))
            t = 8
            if birth == death:
                exact = death*t/(1+death*t)
            else:
                e = np.exp(-(birth-death)*t)
                exact = death*(1-e)/(birth-death*e)
            self.assertAlmostEqual(model.extinction(t)[0], exact, places=10)
            if birth != death:
                eventual, residual = model.eventual_extinction()
                self.assertAlmostEqual(eventual[0], min(1, death/birth), places=9)
                self.assertLess(residual, 1e-10)

    def test_failed_copies_reduce_to_thinned_birth_process(self):
        attempted = Branching(np.zeros((1,1)),np.array([.8]),np.array([.4]),np.array([[.25]]))
        thinned = Branching(np.zeros((1,1)),np.array([.2]),np.array([.4]))
        np.testing.assert_allclose(attempted.extinction(8),thinned.extinction(8),atol=1e-11)
        self.assertAlmostEqual(attempted.reproduction_radius(),.5)

    def test_irrelevant_state_labels_do_not_change_extinction(self):
        transition = np.array([[-.7,.7],[.2,-.2]])
        model = Branching(transition, np.full(2,.8), np.full(2,.4))
        single = Branching(np.zeros((1,1)), np.array([.8]), np.array([.4]))
        np.testing.assert_allclose(model.extinction(8), single.extinction(8)[0], atol=1e-11)
        self.assertAlmostEqual(model.reproduction_radius(), 2)

    def test_cap_is_censored_not_survival(self):
        _, model = trait_model()
        self.assertEqual(model.trial(0,20,0,cap=1), 'censored')

    def test_transport_against_analytic_moments(self):
        source = np.tile([-1.,1.],100000)
        distance = 40
        for mode, expected in [('gated', np.exp(-.01*distance)),
                               ('slow_dial', np.exp(-.005*distance)),
                               ('fast_dial', np.exp(-.3*distance))]:
            child = transmit(source, mode, distance, np.random.default_rng(2))
            self.assertLess(abs(np.mean(source*child)-expected), .01)
        np.testing.assert_array_equal(transmit(source,'slow_dial',0,np.random.default_rng(3)),source)

    def test_scramble_preserves_population_and_work_but_breaks_ancestry(self):
        faithful = generations('slow_dial','faithful',4)
        shuffled = generations('slow_dial','shuffled',4)
        for a,b in zip(faithful,shuffled):
            self.assertEqual(a['mean_response'],b['mean_response'])
            self.assertEqual(a['positive_fraction'],b['positive_fraction'])
            self.assertEqual(a['work_in'],a['work_spent'])
            self.assertAlmostEqual(a['total_flow'],1)
        self.assertGreater(faithful[0]['parent_child_corr'],.8)
        self.assertLess(abs(shuffled[0]['parent_child_corr']),.2)


if __name__ == '__main__':
    unittest.main()
