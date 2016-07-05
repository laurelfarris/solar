import numpy as np

def signif_conf(ts, p):
    ''' Given a timeseries (ts), and desired probability (p),
    compute the standard deviation of ts (s), the number of points in the ts (N),
    the degrees of freedom (DOF), and chi. '''
    s = np.std(ts)
    N = ts.size
    DOF = 2
    chi = chi_sqr(1.-p, DOF)

    signif = ((s**2)*chi) / ((N/2)*DOF)

    return signif
