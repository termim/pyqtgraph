"""
Simple example using BarGraphItem
"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

win = pg.plot()
win.setWindowTitle('pyqtgraph example: BarGraphItem')

x = np.arange(10)
y1 = np.sin(x)
y2 = 1.1 * np.sin(x+1)
y3 = 1.2 * np.sin(x+2)
colors = 'rgb'
colors = range(16)
cm = pg.colormap.get('magma').getLookupTable(nPts=32, mode=pg.ColorMap.QCOLOR)

bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush=colors[0])
bg2 = pg.BarGraphItem(x=x+0.33, height=y2, width=0.3, brush=colors[1])
bg3 = pg.BarGraphItem(x=x+0.66, height=y3, width=0.3, brush=colors[2])

win.addItem(bg1)
win.addItem(bg2)
win.addItem(bg3)

i = 0
def update():
    global i, bg1, bg2, bg3
    i += 1
    for j, bg in enumerate((bg1, bg2, bg3)):
        bg.setPen(colors[i % len(colors)])
        #if i % 10: return
        #bg.setBrush(colors[(i + j) % len(colors)])
ii = 0
def update2():
    global i, ii, bg1, bg2, bg3
    if i % 10: return
    ii += 1
    br = list([pg.mkBrush(cm[(k+ii)%len(x)]) for k in range(len(x))])
    for j, bg in enumerate((bg1, bg2, bg3)):
        bg.setBrush(br)#cm[ii % len(cm)])
        #bg.setBrush(colors[(ii + j) % len(colors)])

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.timeout.connect(update2)
timer.start(300)

# Final example shows how to handle mouse clicks:
class BarGraph(pg.BarGraphItem):
    def mouseClickEvent(self, event):
        print("clicked")


bg = BarGraph(x=x, y=y1*0.3+2, height=0.4+y1*0.2, width=0.8)
win.addItem(bg)

if __name__ == '__main__':
    pg.exec()
