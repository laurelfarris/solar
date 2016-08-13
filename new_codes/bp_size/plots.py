''' Read in size data from file and plot it.  '''
import matplotlib.pyplot as plt
import numpy as np
import math
import pdb

import matplotlib
matplotlib.rc('font',**{'family':'serif','serif':['Times']})
matplotlib.rc('text', usetex=True)

fig, ax = plt.subplots(figsize=(9,6), nrows=2, ncols=3, sharex=True, sharey=True )
plt.figtext(0.5, 0.02, 'distance [pixels]', ha='center')
plt.figtext(0.05, 0.5, 'maximum cross-correlation', rotation=90, va='center')
#ax[1].set_xlabel('distance [pixels]')
#ax[0].set_ylabel('maximum cross-correlation')

waves = (['94', '131', '171'], ['193', '211', '304']) #, '335']

# --> Set axes to a list of ax[0,0], ax[0,1], etc. then in loop,
#      call axes[i] instead of ax[j,k]

#axes = [ ax[0], ax[0], ax[0] ]  #, ax[0][0], ax[0][0], ax[0][0], ax[0][0] ]
#for i in range(0, len(waves)):
for j in range(0,2):
    for k in range(0,3):
        f = open(waves[j][k] + '_bp_sizes.dat')
        x, y, r, c, t = np.loadtxt(f, unpack=True)

        ax[j,k].scatter(r, c, marker='.', s=5, color='black')
        ax[j,k].set_xlim(left=-5, right=max(r))
        ax[j,k].set_ylim(bottom=0.6, top=1.05)
        ax[j,k].tick_params(axis='both',labelsize='small')
        ax[j,k].text(65, max(c), waves[j][k] + ' \AA{} ', ha='right')

plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.show(block=False)
#plt.savefig('size.png', bbox_inches='tight', dpi=300)
