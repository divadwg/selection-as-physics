"""Calibration recovery, stationary weighting and clock invariance."""
import unittest
import numpy as np
from sims.validation.hidden_audit import advance,fit_variance,predict
from sims.validation.run_hidden_map import cdf_power


class HiddenAuditTests(unittest.TestCase):
    def test_variance_fit_recovers_nonunit_normalization(self):
        rng=np.random.default_rng(31);g=rng.uniform(1,3,(128,8));total=np.broadcast_to(g.sum(1)[:,None],g.shape)
        c,q,gamma=.6,1.3,.7;dt=.01
        delta=np.sqrt(2*dt*c*8*g**q/total**gamma)*rng.choice([-1,1],g.shape)
        ids=np.broadcast_to(np.arange(128)[:,None],g.shape)
        data=np.column_stack([ids.ravel(),g.ravel(),total.ravel(),delta.ravel()])
        beta,_,residual=fit_variance(data,dt)
        np.testing.assert_allclose(beta,[np.log(c),q,-gamma],atol=1e-9)
        self.assertLess(residual,1e-9)

    def test_single_route_stationary_prediction(self):
        beta=np.array([0.,1.3,-.7])
        cuts,p,f,_=predict(beta,n=1,count=100000,seed=4)
        target=cdf_power(cuts,.7-1.3,3)
        self.assertLess(np.max(abs(p-target)),.008)
        np.testing.assert_allclose(p,f)

    def test_common_activity_rescales_clock(self):
        rng=np.random.default_rng(5);g=rng.uniform(1,3,(32,8));x=rng.random(g.shape);y=rng.random(g.shape)
        a=advance(g,x,y,1.5,1/512,activity=1)
        b=advance(g,x,y,1.5,1/2048,activity=4)
        for left,right in zip(a,b):np.testing.assert_array_equal(left,right)


if __name__=='__main__':unittest.main()
