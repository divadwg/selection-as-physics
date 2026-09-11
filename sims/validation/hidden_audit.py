"""Calibrate deterministic coarse increments, then predict independent ensembles.

The fitted zero-drift diffusion is a candidate approximation. Diagnostics retain
conditional drift and correlations rather than assuming stationarity proves it.
Uncertainty clusters by independently initialised ensemble, preserving dependence
between its routes and sampled times.
"""
import numpy as np
from .hidden_map import hidden_step,reflect_box


def advance(g,x,y,q,dt,activity=1.,upper=3.):
    x,y=hidden_step(x,y)
    noise=np.sqrt(2)*np.cos(2*np.pi*x)
    diffusion=activity*g.shape[1]*g**q/g.sum(axis=1,keepdims=True)
    delta=np.sqrt(2*dt*diffusion)*noise
    safe=(g-1>2*np.sqrt(dt*diffusion))&(upper-g>2*np.sqrt(dt*diffusion))
    return reflect_box(g+delta,upper=upper),x,y,delta,noise,safe


def calibrate(q,dt,count=256,seed=310,upper=3.,burn=4.,duration=4.):
    rng=np.random.default_rng(seed)
    x=rng.random((count,8));y=rng.random((count,8));g=np.full_like(x,2.)
    records=[];driver_history=[];lag_products={lag:np.zeros(count) for lag in [1,2,4,8]}
    lag_counts={lag:0 for lag in lag_products};cross=np.zeros(count);cross_count=0
    for t in range(round((burn+duration)/dt)):
        previous=g
        g,x,y,delta,noise,safe=advance(g,x,y,q,dt,upper=upper)
        if t*dt>=burn:
            for lag in lag_products:
                if len(driver_history)>=lag:
                    lag_products[lag]+=np.mean(noise*driver_history[-lag],axis=1);lag_counts[lag]+=1
            cross+=np.mean(noise[:,::2]*noise[:,1::2],axis=1);cross_count+=1
            if t%32==0:
                ids=np.broadcast_to(np.arange(count)[:,None],g.shape)
                total=np.broadcast_to(previous.sum(axis=1,keepdims=True),g.shape)
                records.append(np.column_stack([ids[safe],previous[safe],total[safe],delta[safe]]))
        driver_history.append(noise)
        if len(driver_history)>8:driver_history.pop(0)
    data=np.concatenate(records)
    diagnostics={f'driver_lag_{lag}':v/lag_counts[lag] for lag,v in lag_products.items()}
    diagnostics['driver_adjacent_routes']=cross/cross_count
    return data,diagnostics


def fit_variance(data,dt,n=8):
    ids=data[:,0].astype(int);g,total,delta=data[:,1:].T
    X=np.column_stack([np.ones(len(g)),np.log(g),np.log(total)])
    target=delta**2/(2*dt*n)
    beta=np.linalg.lstsq(X,np.log(np.maximum(target,1e-30)),rcond=None)[0]
    beta[0]+=np.log(2)
    for _ in range(30):
        ratio=target/np.exp(X@beta)
        score=X.T@(ratio-1)
        jac=X.T@(X*ratio[:,None])
        change=np.linalg.solve(jac,score)
        beta+=change
        if np.max(abs(change))<1e-10:break
    ratio=target/np.exp(X@beta)
    cluster=np.zeros((ids.max()+1,3));np.add.at(cluster,ids,X*(ratio-1)[:,None])
    jac=X.T@(X*ratio[:,None]);inverse=np.linalg.inv(jac)
    clusters=len(cluster)
    covariance=clusters/(clusters-1)*inverse@(cluster.T@cluster)@inverse.T
    return beta,covariance,float(np.max(abs(X.T@(ratio-1)))/len(g))


def drift_bins(data,dt,bins=(1,1.5,2,2.5,3)):
    rows=[];ids=data[:,0].astype(int);count=ids.max()+1
    for lo,hi in zip(bins[:-1],bins[1:]):
        keep=(data[:,1]>=lo)&(data[:,1]<hi)
        weights=np.bincount(ids[keep],minlength=count)
        sums=np.bincount(ids[keep],weights=data[keep,3]/dt,minlength=count)
        mean=sums.sum()/weights.sum()
        se=np.sqrt(count/(count-1)*np.sum((sums-mean*weights)**2))/weights.sum()
        rows.append(dict(lo=lo,hi=hi,count=int(weights.sum()),drift=float(mean),cluster_se=float(se)))
    return rows


def heldout(q,dt,initial,seed,count=256,upper=3.,horizon=32.,activity=1.):
    rng=np.random.default_rng(seed);x=rng.random((count,8));y=rng.random((count,8))
    value={'low':1.,'middle':(1+upper)/2,'high':upper}[initial]
    g=np.full_like(x,value);snapshots={}
    steps=round(horizon/dt)
    for t in range(steps):
        g,x,y,*_=advance(g,x,y,q,dt,activity=activity,upper=upper)
        if t+1 in [steps//2,steps]:snapshots[(t+1)*dt]=g.copy()
    return snapshots


def sample_power(exponent,upper,size,rng):
    u=rng.random(size);a=exponent+1
    return upper**u if abs(a)<1e-10 else (1+u*np.expm1(a*np.log(upper)))**(1/a)


def predict(beta,upper=3.,n=8,count=100000,seed=811):
    """Exact reference proposal pi_1 reweighted to pi_gamma, using measured q,gamma.

    D=c*N*g^q/S^gamma has zero-current density proportional to S^gamma*prod g^-q.
    This remains a zero-drift model prediction; measured drift is checked separately.
    """
    rng=np.random.default_rng(seed);q=beta[1];gamma=-beta[2]
    g=sample_power(-q,upper,(count,n),rng)
    g[np.arange(count),rng.integers(n,size=count)]=sample_power(1-q,upper,count,rng)
    weight=g.sum(axis=1)**(gamma-1);weight/=weight.sum()
    cuts=np.linspace(1,upper,101);share=g/g.sum(axis=1,keepdims=True)
    p=np.array([weight@((g<=a).mean(axis=1)) for a in cuts])
    f=np.array([weight@((share*(g<=a)).sum(axis=1)) for a in cuts])
    return cuts,p,f,float(1/np.sum(weight**2))


def assess(g,cuts,p,f):
    share=g/g.sum(axis=1,keepdims=True)
    observed_p=np.array([(g<=a).mean() for a in cuts])
    observed_f=np.array([(share*(g<=a)).sum(axis=1).mean() for a in cuts])
    return float(np.max(abs(observed_p-p))),float(np.max(abs(observed_f-f))),observed_p,observed_f
