"""Draw retained comparisons with ReportLab; flow paths use the frozen final field."""
from pathlib import Path
import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


def main():
    directory = Path('docs/material_results')
    c = canvas.Canvas(str(directory/'material_flow.pdf'), pagesize=(900, 470))
    c.setFont('Helvetica', 17)
    c.drawString(32, 438, 'Binary material can maintain an obstruction to flow')
    for x, title in zip([32, 290, 548], ['Prepared material', 'After 140 local sweeps', 'Flow: final snapshot']):
        c.setFont('Helvetica', 12); c.drawString(x, 405, title)
    for row, (name, label) in enumerate([('patch_0', 'With cohesion'), ('no_cohesion', 'Without cohesion')]):
        data = np.load(directory/(name+'.npz')); y0 = 222-row*174
        c.setFillColorRGB(0, 0, 0); c.setFont('Helvetica', 10); c.drawString(32, y0+153, label)
        for column, key in enumerate(['initial_bits', 'final_bits', 'fraction']):
            x0 = 32+258*column; width, height = 230, 142
            xmin, xmax, ymin, ymax = (24, 48, 18, 43) if column < 2 else (24, 76, 15, 46)
            actual_width = height*(xmax-xmin)/(ymax-ymin)
            if actual_width > width:
                height = width*(ymax-ymin)/(xmax-xmin)
            else:
                x0 += (width-actual_width)/2
                width = actual_width
            scale = 4 if column < 2 else 1
            field = data[key][xmin*scale:xmax*scale, ymin*scale:ymax*scale]
            pixels = (255*(1-field.T[::-1])).astype('uint8')
            c.drawImage(ImageReader(Image.fromarray(pixels)), x0, y0, width, height)
            if column == 2:
                def point(x, y):
                    return x0+(x-xmin)*width/(xmax-xmin), y0+(y-ymin)*height/(ymax-ymin)
                c.setStrokeColorRGB(.18, .41, .59); c.setLineWidth(.5)
                for x in range(xmin+2, xmax-1, 3):
                    for y in range(ymin+1, ymax-1, 3):
                        if data['fraction'][x, y] > 0: continue
                        vx, vy = data['ux'][x,y], data['uy'][x,y]
                        speed = np.hypot(vx,vy)
                        if speed < 1e-6: continue
                        dx, dy = vx/speed, vy/speed
                        a, b = point(x, y); e, f = point(x+1.3*dx, y+1.3*dy)
                        c.line(a, b, e, f)
                        c.line(e, f, e-2*dx+dy, f-2*dy-dx)
                        c.line(e, f, e-2*dx-dy, f-2*dy+dx)
                c.setStrokeColorRGB(.8, .29, .06); c.setLineWidth(.6)
                ids = np.flatnonzero(data['returned'])
                for i in ids[::max(1,len(ids)//5)][:5]:
                    track = data['tracks'][:,i]; path = c.beginPath(); started = False
                    for x, y in track:
                        if not (xmin <= x <= xmax and ymin <= y <= ymax):
                            started = False; continue
                        if started: path.lineTo(*point(x,y))
                        else: path.moveTo(*point(x,y)); started = True
                    c.drawPath(path)
            c.setStrokeColorRGB(.65,.65,.65); c.setLineWidth(.5); c.rect(x0,y0,width,height)
    c.setFillColorRGB(.2,.2,.2); c.setFont('Helvetica', 9)
    c.drawString(32, 25, 'Same starting material in both rows. Blue: velocity direction. Orange: selected returning paths in the frozen final field.')
    c.drawString(32, 12, 'The substrate supports the material. These runs test persistence from a prepared patch, not spontaneous formation from uniform noise.')
    c.save()


if __name__ == '__main__':
    main()
