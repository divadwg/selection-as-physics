"""Structural checks for the deterministic-map pilot."""
import unittest
import numpy as np
from sims.validation.hidden_map import hidden_step,reflect_box,simulate


class HiddenMapTests(unittest.TestCase):
    def test_torus_map_has_inverse(self):
        rng=np.random.default_rng(2);x=rng.random(1000);y=rng.random(1000)
        a,b=hidden_step(x,y)
        np.testing.assert_allclose((a-b)%1,x,atol=1e-14)
        np.testing.assert_allclose((-a+2*b)%1,y,atol=1e-14)

    def test_reflection_handles_multiple_crossings(self):
        np.testing.assert_allclose(reflect_box(np.array([-3.,0.,1.,2.,3.,4.,7.])),[1,2,1,2,3,2,3])

    def test_reproducible_evolution_with_fixed_initial_state(self):
        a,_=simulate(1.5,1/128,count=8,horizon=1,seed=4)
        b,_=simulate(1.5,1/128,count=8,horizon=1,seed=4)
        for t in a:np.testing.assert_array_equal(a[t],b[t])


if __name__=='__main__':unittest.main()
