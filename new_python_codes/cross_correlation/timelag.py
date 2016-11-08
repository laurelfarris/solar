'''
Programmer:         R.T.James McAteer and Peter Gallager (translated by Laurel Farris)
Purpose:            Calculate maxiumum cross-correlation of two lightcurves
Useage:             timelag, timeseries1, timeseries2, array of possible timelags, result
Output:             Result, an array of cross-correlation values for each timelag
'''

import numpy as np


def timelag(x, xs, tau, maxcor):
    maxcor = np.zeros(2)
    c = np.zeros(tau.size)
