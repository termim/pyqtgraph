# -*- coding: utf-8 -*-
"""
Demonstrates selecting plot curves by mouse click
"""
import initExample ## Add path to library (just for examples; you do not need this)

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

win = pg.plot()
win.setWindowTitle('pyqtgraph example: Plot data selection')

curves = [
    pg.PlotCurveItem(y=np.sin(np.linspace(0, 20, 1000)), pen='r', clickable=True),
    pg.PlotCurveItem(y=np.sin(np.linspace(1, 21, 1000)), pen='g', clickable=True),
    pg.PlotCurveItem(y=np.sin(np.linspace(2, 22, 1000)), pen='b', clickable=True),
    pg.MonochromeBarGraphItem(x=np.arange(10, 1000, 200), y=0, height=np.ones(5), width=50, pen='y', clickable=True)
    ]

def plotClicked(curve):
    global curves
    for i,c in enumerate(curves):
        if c is curve:
            c.setPen('rgbm'[i], width=3)
            c.setBrush('m')
        else:
            c.setPen('rgby'[i], width=1)
            c.setBrush((128, 128, 128))


for c in curves:
    win.addItem(c)
    c.sigClicked.connect(plotClicked)
curves[-1].getViewBox().enableAutoRange(enable=False)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
