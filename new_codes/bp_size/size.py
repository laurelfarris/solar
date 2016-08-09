''' Read in size data from file and plot it.  '''
import matplotlib.pyplot as plt
import numpy as np
import math
import pdb

#import matplotlib
#matplotlib.rc('font',**{'family':'serif','serif':['Times']})
#matplotlib.rc('text', usetex=True)

fig, ax = plt.subplots()
ax.set_xlabel('distance [pixels]')
ax.set_ylabel('intensity [arbitrary]')
ax.tick_params(axis='both',labelsize='small')

f = open('bp_sizes.dat')
r, c, t = np.loadtxt(f, unpack=True)
ax.scatter(r, c, marker='.', s=2, color='black')
plt.show()
#plt.savefig('size.png',dpi=300)
