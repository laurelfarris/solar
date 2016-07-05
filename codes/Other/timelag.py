# Programmer:       Laurel Farris
# Last modified:    19 January 2016
# Description:      This module can be called to calculate the 
#                   maximum cross-correlation (cc) of two lightcurves.
#

import numpy as np
import pdb
import math
import matplotlib.pyplot as plt

# input x, xs (lightcurves 1 and 2), and tau (the timelag).
# c and maxcor are output values... though c may not be necessary.
def timelag(x, xs, tau):
    maxcor = np.zeros(2)
    c = np.zeros(len(tau))  # cc value
    mx = np.mean(x)
    mxs = np.mean(xs)

    # Calculate the cc
    for i in range(0, len(tau)):
        c[i] = np.sum( (x-mx) * np.roll( (xs-mxs),tau[i] )  ) /
               np.sqrt( np.sum((x-mx)**2 * np.sum(x-mxs)**2)  )

    # Create plot of cc as a function of tau (the timelag)
    # Comment this out if plots are not needed, particularly if this
    # function is called in a loop with many lightcurves.
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(tau, c)
    ax.show()

    # Find the best cc value and insert it into the output array, maxcor.
    bestcor = c.index(max(c))
    if (len(bestcor) != max(c)):
        print tau[bestcor], c[bestcor]
        bestcor = np.median(bestcor)

    maxcor[0] = tau[bestcor]
    maxcor[1] = c[bestcor]

    return c, maxcor
