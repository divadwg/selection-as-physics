"""D2Q9 equilibrium used by the existing flow-past-a-pole experiment.

These standard velocity moments restore the missing helper. No replacement for
its undocumented vortex counter is supplied: vorticity alone is not a loop test.
"""
import numpy as np
cx=np.array([0,1,0,-1,0,1,-1,-1,1])
cy=np.array([0,0,1,0,-1,1,1,-1,-1])
w=np.array([4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36])
opp=np.array([0,3,4,1,2,7,8,5,6])


def equilibrium(rho,ux,uy,linear=False):
    cu=3*(cx[:,None,None]*ux+cy[:,None,None]*uy)
    result=1+cu
    if not linear:
        result=result+.5*cu**2-1.5*(ux**2+uy**2)
    return w[:,None,None]*rho*result
