"""Calibration uses seed 310; prediction samples and held-out runs use other seeds."""
from pathlib import Path
import hashlib,json
import numpy as np
from .hidden_audit import calibrate,fit_variance,drift_bins,heldout,predict,assess
from .run_heredity import write_csv


def main():
    out=Path('docs/hidden_audit_results');out.mkdir(parents=True,exist_ok=True)
    fits=[];drifts=[];correlations=[];checks=[]
    for q in [.5,1.,1.5,2.5]:
        for dt in [1/512,1/2048]:
            data,diag=calibrate(q,dt)
            beta,cov,residual=fit_variance(data,dt)
            tag=f'q{q}_dt{dt}'
            np.savez_compressed(out/(tag+'_calibration.npz'),data=data,beta=beta,covariance=cov,**diag)
            fits.append(dict(q_supplied=q,dt=dt,c_fitted=float(np.exp(beta[0])),q_fitted=float(beta[1]),
                gamma_fitted=float(-beta[2]),log_c_se=float(np.sqrt(cov[0,0])),
                q_se=float(np.sqrt(cov[1,1])),gamma_se=float(np.sqrt(cov[2,2])),
                samples=len(data),independent_ensembles=256,moment_residual=residual))
            drifts.extend([dict(q=q,dt=dt,**row) for row in drift_bins(data,dt)])
            for name,values in diag.items():
                correlations.append(dict(q=q,dt=dt,observable=name,mean=float(values.mean()),
                    cluster_se=float(values.std(ddof=1)/np.sqrt(len(values)))))
            print('FIT',fits[-1],flush=True)
            if dt!=1/2048:continue
            cuts,p,f,ess=predict(beta)
            _,p2,f2,_=predict(beta,seed=812)
            np.savez_compressed(out/(tag+'_prediction.npz'),cuts=cuts,occupancy=p,flow=f)
            for index,initial in enumerate(['low','middle','high']):
                snapshots=heldout(q,dt,initial,seed=910+index)
                for time,g in snapshots.items():
                    ep,ef,op,of=assess(g,cuts,p,f)
                    checks.append(dict(q=q,dt=dt,initial=initial,time=time,replicas=len(g),
                        occupancy_cdf_error=ep,flow_cdf_error=ef,reference_ess=ess,
                        reference_seed_cdf_difference=float(max(np.max(abs(p-p2)),np.max(abs(f-f2))))))
                    np.savez_compressed(out/(tag+f'_{initial}_t{time}.npz'),g=g,occupancy=op,flow=of)
                print('CHECK',checks[-1],flush=True)
    for name,rows in [('fits',fits),('drift',drifts),('correlations',correlations),('heldout',checks)]:
        write_csv(out/(name+'.csv'),rows)
    files=[Path(__file__),Path(__file__).with_name('hidden_audit.py'),Path(__file__).with_name('hidden_map.py')]
    (out/'manifest.json').write_text(json.dumps(dict(calibration_seed=310,heldout_seeds=[910,911,912],
        prediction_seeds=[811,812],calibration_burn=4,calibration_duration=4,sampling_stride=32,
        heldout_horizon=32,n=8,upper=3,ensembles=256,
        source_sha256={str(p.relative_to(Path(__file__).resolve().parents[2])):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n')


if __name__=='__main__':main()
