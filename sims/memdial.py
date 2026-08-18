"""
Memory as a dial. One lattice flow layer, no bed. The update gets one extra term:
a force pulling velocity toward a memory field um that is itself written from u.
  linear write : um <- um + (u-um)/T                    (always writes, always forgets)
  gated write  : um <- um + (u-um)/T only where |u-um|>theta   (writes only big changes)
Kick a vortex pair into a quiet channel, remove the kick, watch the circulation decay.
"""
import numpy as np, sys
cx=np.array([0,1,0,-1,0,1,-1,-1,1]); cy=np.array([0,0,1,0,-1,1,1,-1,-1])
w=np.array([4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36]); opp=np.array([0,3,4,1,2,7,8,5,6])
def feq(rho,ux,uy):
    cu=3*(cx[:,None,None]*ux+cy[:,None,None]*uy)
    return w[:,None,None]*rho*(1+cu+0.5*cu**2-1.5*(ux**2+uy**2))
def run(k, T=200, theta=None, nx=120, ny=60, tau=0.6, steps=4000, kick_until=300, A=2e-4, seed=0):
    om=1/tau; X,Y=np.meshgrid(np.arange(nx),np.arange(ny),indexing='ij')
    f=feq(np.ones((nx,ny)),np.zeros((nx,ny)),np.zeros((nx,ny)))
    umx=np.zeros((nx,ny)); umy=np.zeros((nx,ny))
    # kick: localised transverse force with sign flip across the middle -> a counter-rotating pair
    x0,y0=nx//2,ny//2; g=np.exp(-((X-x0)**2+(Y-y0)**2)/50.0)
    Fkx=A*g*np.sign(Y-y0+0.5); Fky=np.zeros_like(Fkx)
    circ=[]; wall=np.zeros((nx,ny),bool); wall[:,0]=True; wall[:,-1]=True
    for t in range(steps):
        rho=f.sum(0); ux=(cx[:,None,None]*f).sum(0)/rho; uy=(cy[:,None,None]*f).sum(0)/rho
        # memory write
        dx=umx-ux; dy=umy-uy
        if theta is None: umx-=dx/T; umy-=dy/T
        else:
            m=np.hypot(dx,dy)>theta; umx[m]-=dx[m]/T; umy[m]-=dy[m]/T
        Fx=k*(umx-ux); Fy=k*(umy-uy)
        if t<kick_until: Fx=Fx+Fkx
        f=f-om*(f-feq(rho,ux+tau*Fx,uy+tau*Fy))
        fw=f[:,wall]; f[:,wall]=fw[opp]
        for i in range(9): f[i]=np.roll(np.roll(f[i],cx[i],axis=0),cy[i],axis=1)
        if t%50==0:
            vort=np.gradient(uy,axis=0)-np.gradient(ux,axis=1)
            circ.append((t,float(np.abs(vort[x0-15:x0+15,y0-15:y0+15]).sum())))
    return np.array(circ)
if __name__=="__main__":
    import json
    out={}
    for label,k,theta in [('none',0.0,None),('lin_k0.002',0.002,None),('lin_k0.01',0.01,None),('lin_k0.03',0.03,None),
                          ('gate_k0.01',0.01,3e-4),('gate_k0.03',0.03,3e-4)]:
        c=run(k,theta=theta); out[label]=c.tolist(); print(label, 'circ at kick end',round(c[6,1],4),'at 2000',round(c[40,1],4),'at 3950',round(c[-1,1],4),flush=True)
    json.dump(out,open('/home/claude/memdial.json','w'))
