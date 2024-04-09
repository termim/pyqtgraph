"""
Simple example using BarGraphItem
"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

win = pg.plot()
win.setWindowTitle('pyqtgraph example: BarGraphItem')

N=15
max = 3*np.pi
x=np.arange(0, max, max/N)
d = max/N/3
w = d
y1 = np.sin(x)
y2 = np.sin(x+d)
y3 = np.sin(x+2*d)

colors = range(16)
cm = pg.colormap.get('plasma').getLookupTable(nPts=len(x)*2, mode=pg.ColorMap.QCOLOR)
bc = list([ pg.mkBrush(cm[i]) for i in range(len(cm)) ])

bg1 = pg.BarGraphItem(x=x, height=y1, width=w, brush=colors[0])
bg2 = pg.BarGraphItem(x=x+d, height=y2, width=w, brush=colors[1])
bg3 = pg.BarGraphItem(x=x+2*d, height=y3, width=w, brush=colors[2])

win.addItem(bg1)
win.addItem(bg2)
win.addItem(bg3)

i = 0
def update_pen():
    global i, bg1, bg2, bg3
    i += 1
    for j, bg in enumerate((bg1, bg2, bg3)):
        bg.setPen(colors[i % len(colors)], width=i%6)

timer1 = QtCore.QTimer()
timer1.timeout.connect(update_pen)
timer1.start(500)

ii = 0
def update_brush():
    global ii, bg1, bg2, bg3
    ii += 1
    ic0 = ii % len(bc)
    for j, bg in enumerate((bg1, bg2, bg3)):
        ic0 = (ii+j) % len(bc)
        br = list([bc[(ic0+ic)%len(bc)] for ic in range(len(x))])
        bg.setBrush(br)

timer2 = QtCore.QTimer()
timer2.timeout.connect(update_brush)
timer2.start(500)

# Final example shows how to handle mouse clicks:
class BarGraph(pg.BarGraphItem):
    def mouseClickEvent(self, event):
        print("clicked")


bg = BarGraph(x=x, y=y1*w+2, height=0.4+y1*0.2, width=w*2.4)
win.addItem(bg)

if __name__ == '__main__':
    pg.exec()
