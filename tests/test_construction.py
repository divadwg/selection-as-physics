"""Conservation and analytic controls for the spatial examples."""
import unittest
import numpy as np
from sims.validation.construction import drainage,laplacian,reaction_step,components
from sims.boundaries.lg import equilibrium,cx,cy
from sims.validation.run_pole_flow import trace_returns


class ConstructionTests(unittest.TestCase):
    def test_runoff_stops_at_pits_and_conserves_rain(self):
        z=np.array([[0.,0.,0.],[3.,1.,3.],[4.,0.5,4.]])
        rain=np.ones_like(z);rain[0]=0
        q,dest,_=drainage(z,rain)
        self.assertEqual(dest[2,1],-1)
        self.assertAlmostEqual(q[dest<0].sum(),rain.sum())
        for i,j in enumerate(dest.ravel()):
            if j>=0:self.assertGreater(z.ravel()[i],z.ravel()[j])

    def test_periodic_diffusion_conserves_amount(self):
        a=np.random.default_rng(4).random((20,30))
        self.assertAlmostEqual(laplacian(a).sum(),0,places=12)

    def test_reaction_balances_and_homogeneous_fixed_point(self):
        rng=np.random.default_rng(3);u=rng.random((20,20));v=rng.random((20,20))
        un,vn=reaction_step(u,v,dt=.1)
        expected=.1*(.03*(1-u).sum()-(.03+.062)*v.sum())
        self.assertAlmostEqual((un+vn-u-v).sum(),expected,places=11)
        un,vn=reaction_step(np.ones((8,8)),np.zeros((8,8)))
        np.testing.assert_array_equal(un,1);np.testing.assert_array_equal(vn,0)

    def test_components_join_periodic_boundary(self):
        mask=np.zeros((8,8),bool);mask[0,3]=True;mask[-1,3]=True
        self.assertEqual(len(components(mask,periodic=True)[1]),1)
        self.assertEqual(len(components(mask,periodic=False)[1]),2)

    def test_lattice_equilibrium_moments(self):
        rho=np.full((4,5),1.1);ux=np.full((4,5),.03);uy=np.full((4,5),-.02)
        for linear in [False,True]:
            f=equilibrium(rho,ux,uy,linear)
            np.testing.assert_allclose(f.sum(0),rho,atol=1e-14)
            np.testing.assert_allclose((cx[:,None,None]*f).sum(0),rho*ux,atol=1e-14)
            np.testing.assert_allclose((cy[:,None,None]*f).sum(0),rho*uy,atol=1e-14)

    def test_tracer_detects_rotation_but_not_straight_flow(self):
        x,y=np.indices((60,60));solid=np.zeros((60,60),bool)
        count,_,_=trace_returns(-.01*(y-30),.01*(x-30),solid,20,30,3,steps=1000)
        self.assertGreater(count,0)
        count,_,_=trace_returns(np.full((60,60),.03),np.zeros((60,60)),solid,20,30,3,steps=1000)
        self.assertEqual(count,0)


if __name__=='__main__':unittest.main()
