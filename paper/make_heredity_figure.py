"""Plot retained threshold calculations; no fitted or empirical curves."""
import csv
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

root=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((root/'docs/heredity_results/restoration_reversal.csv').open()))
out=canvas.Canvas(str(root/'paper/heredity_threshold.pdf'),pagesize=(468,205))
for panel,damage in enumerate(['state_dependent','constant']):
    x0=42+panel*231; y0=40; width=176; height=135
    def point(t,v): return x0+t/60*width,y0+v/1.7*height
    out.setFont('Helvetica',9)
    out.setFillColor(HexColor('#222222'))
    out.drawCentredString(x0+width/2,192,['Damage grows with activity','Damage independent of activity'][panel])
    out.setStrokeColor(HexColor('#bbbbbb'));out.setLineWidth(.4)
    for y in [0,.5,1,1.5]:
        xx,yy=point(0,y);out.line(xx,yy,xx+width,yy)
        out.drawRightString(xx-5,yy-3,str(y))
    for t in [0,20,40,60]:
        xx,yy=point(t,0);out.drawCentredString(xx,yy-13,str(t))
    out.drawCentredString(x0+width/2,10,'Transit time')
    for k,color in [('0.0','#225ea8'),('0.7','#d95f0e')]:
        selected=[r for r in rows if r['intervals']=='64' and r['damage']==damage and r['restoring']==k]
        coords=[point(float(r['transit']),float(r['critical_copy_coefficient'])) for r in selected]
        out.setStrokeColor(HexColor(color));out.setFillColor(HexColor(color));out.setLineWidth(1.4)
        path=out.beginPath();path.moveTo(*coords[0])
        for xy in coords[1:]:path.lineTo(*xy)
        out.drawPath(path)
        for xy in coords:out.circle(*xy,2,stroke=0,fill=1)
        out.drawString(x0+5,166-(k=='0.7')*13,'Restoration '+k)
    out.saveState();out.setFillColor(HexColor('#222222'));out.translate(x0-29,y0+height/2);out.rotate(90)
    out.drawCentredString(0,0,'Critical copying coefficient');out.restoreState()
out.save()
