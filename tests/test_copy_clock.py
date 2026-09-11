"""Renewal and work-accounting checks for copying clocks."""
import unittest
import numpy as np
from sims.validation.copy_clock import reproduction,offspring


class CopyClockTests(unittest.TestCase):
    def test_accumulator_matches_survival_weighted_birth_schedule(self):
        for p in [.2,.8,1.]:
            numerical=p*np.exp(-.4*np.arange(1,2000)).sum()
            self.assertAlmostEqual(numerical,reproduction(1,.4,1,p))
            self.assertAlmostEqual(reproduction(1,np.log1p(p),1,p),1)

    def test_clock_can_change_establishment_classification(self):
        self.assertLess(reproduction(1,.7,1,.8,'accumulator'),1)
        self.assertGreater(reproduction(1,.7,1,.8,'poisson'),1)

    def test_accumulator_never_spends_unreceived_work(self):
        lifetime,attempts,viable=offspring(1,.7,1,.8,'accumulator',5000,4)
        self.assertTrue(np.all(attempts*.7<=lifetime))
        self.assertTrue(np.all(viable<=attempts))
        self.assertTrue(np.all(attempts[lifetime<.7]==0))


if __name__=='__main__':unittest.main()
