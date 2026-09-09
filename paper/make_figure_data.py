"""Generate Figure 1 data from the tested stationary formula, not dynamics."""
import csv
from pathlib import Path
import sys

import numpy as np
from reportlab.graphics.shapes import Drawing, String, Line
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF
from reportlab.lib import colors

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from sims.validation.conserved_flow import continuum_half


def main():
    target = Path(__file__).with_name("window_data.csv")
    series = [[], [], []]
    with target.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["q", "base_r100", "base_r1e8", "n40_r1e8"])
        for q in np.linspace(0, 3, 301):
            small = continuum_half(1, q, 100)
            large = continuum_half(1, q, 1e8)
            writer.writerow([f"{q:.2f}", f"{small:.12g}", f"{large:.12g}",
                             f"{(39/40)*large + 1/80:.12g}"])
            for line, value in zip(series, [small, large, (39/40)*large+1/80]):
                line.append((float(q), float(np.log10(value))))
    drawing = Drawing(500, 300)
    chart = LinePlot()
    chart.x, chart.y, chart.width, chart.height = 64, 74, 420, 212
    chart.data = series
    chart.xValueAxis.valueMin, chart.xValueAxis.valueMax = 0, 3
    chart.xValueAxis.valueSteps = [0, 0.5, 1, 1.5, 2, 2.5, 3]
    chart.yValueAxis.valueMin, chart.yValueAxis.valueMax = -6, 0
    chart.yValueAxis.valueSteps = list(range(-6, 1))
    chart.yValueAxis.labelTextFormat = lambda x: f"{10**x:g}"
    chart.yValueAxis.visibleGrid = True
    chart.yValueAxis.gridStrokeColor = colors.HexColor("#dddddd")
    chart.yValueAxis.gridStrokeWidth = 0.4
    for axis in [chart.xValueAxis, chart.yValueAxis]:
        axis.labels.fontName = "Times-Roman"
        axis.labels.fontSize = 10
    palette = [colors.HexColor("#255886"), colors.black, colors.HexColor("#b36016")]
    for i, color in enumerate(palette):
        chart.lines[i].strokeColor = color
        chart.lines[i].strokeWidth = 1.5
    chart.lines[2].strokeDashArray = [5, 3]
    drawing.add(chart)
    for q in [1, 2]:
        x = chart.x + q * chart.width / 3
        drawing.add(Line(x, chart.y, x, chart.y+chart.height,
                         strokeColor=colors.grey, strokeDashArray=[2, 3], strokeWidth=0.7))
    drawing.add(String(274, 44, "Noise exponent q (m = 1)",
                       textAnchor="middle", fontName="Times-Roman", fontSize=12))
    from reportlab.graphics.shapes import Group
    ylabel = Group(String(0, 0, "Pooled half-flow population fraction",
                          textAnchor="middle", fontName="Times-Roman", fontSize=12))
    ylabel.rotate(90)
    ylabel.translate(180, -13)
    drawing.add(ylabel)
    for i, (label, color) in enumerate(zip(["P0, R = 100", "P0, R = 100 million", "P40, R = 100 million"], palette)):
        x = 44 + 158*i
        drawing.add(Line(x, 15, x+18, 15, strokeColor=color, strokeWidth=1.5,
                         strokeDashArray=[5, 3] if i==2 else None))
        drawing.add(String(x+23, 12, label, fontName="Times-Roman", fontSize=10))
    figure = target.with_name("window_figure.pdf")
    renderPDF.drawToFile(drawing, str(figure))
    print(target)
    print(figure)


if __name__ == "__main__":
    main()
