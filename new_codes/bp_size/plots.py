''' Read in size data from file and plot it.  '''
import matplotlib.pyplot as plt
import numpy as np
import math
import pdb
import matplotlib.ticker as mtick

import matplotlib
matplotlib.rc('font',**{'family':'serif','serif':['Times']})
matplotlib.rc('text', usetex=True)

fig, ax = plt.subplots(figsize=(12,8), nrows=2, ncols=3, sharex=True, sharey=True )

waves = ['94', '131', '171', '193', '211', '304'] #, '335']
axes = [ax[0][0], ax[0][1], ax[0][2], ax[1][0], ax[1][1], ax[1][2]]

fontsize=15
tfont=12
for i in range(0, len(waves)):
    f = open(waves[i] + '_bp_sizes.dat')
    x, y, r, cor, t = np.loadtxt(f, unpack=True)
    m = axes[i].scatter(r, cor, c=t, vmin=min(t), vmax=max(t),
                    cmap='viridis', s=3, lw=0)
    axes[i].axis('tight')  # no extra space between data points and axes

    majorLocator = mtick.LinearLocator(numticks=10)

    axes[i].xaxis.set_major_locator(majorLocator)
    #axes[i].xaxis.set_minor_locator(minorLocator)

    axes[i].yaxis.set_major_locator(majorLocator)
    #axes[i].yaxis.set_minor_locator(minorLocator)

    axes[i].minorticks_on()
    axes[i].tick_params(axis='both', which='minor', direction='in', length=4)
    axes[i].tick_params(axis='both', which='major', direction='in', length=6)
    #axes[i].set_xticks(np.arange(0,80,10), minor=True)
    #axes[i].set_xticklabels(fontsize=tfont)
    #axes[i].set_yticklabels(np.arange(0,1,0.1),fontsize=tfont)
    axes[i].text(68, 0.93, waves[i] + ' \AA{} ', ha='right')

fig.text(0.5, 0.03, 'radius [pixels]', ha='center', fontsize=fontsize)
fig.text(0.08, 0.5, 'maximum cross-correlation', va='center', rotation='vertical', fontsize=fontsize)

cax = fig.add_axes([0.93, 0.10, 0.02, 0.80])
step = 30
cbar = fig.colorbar(m, cax=cax)
#cbar.set_ticks(np.arange(min(t),max(t)+step,step))
#cbar.set_ticklabels(np.arange(min(t),max(t)+step,0.5*step))
#cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar


plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.show(block=False)
#plt.savefig('size.png', bbox_inches='tight', dpi=300)
