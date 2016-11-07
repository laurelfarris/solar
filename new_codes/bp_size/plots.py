''' Read in size data from file and plot it.  '''
import matplotlib.pyplot as plt
import numpy as np
import math
import pdb
import matplotlib.ticker as mtick
from matplotlib.ticker import FormatStrFormatter

#import matplotlib
#matplotlib.rc('font',**{'family':'serif','serif':['Times']})
#matplotlib.rc('text', usetex=True)
#fig, ax = plt.subplots(figsize=(8,12), nrows=3, ncols=2, sharex=True, sharey=True)

fig = plt.figure(figsize=(8,10))
fontsize=14
waves = ['94', '131', '171', '193', '211', '304'] #, '335']
for i in range(0, len(waves)):
    f = open(waves[i] + '_bp_sizes.dat')
    x, y, r, cor, t = np.loadtxt(f, unpack=True)
    ax = fig.add_subplot(3,2,i+1)
    m = ax.scatter(r, cor, c=t, vmin=min(t), vmax=max(t),
                    cmap='viridis', s=2, lw=0)
    #ax.axis('tight')
    '''
    ax.set_xlim(left=-5, right=max(r))
    ax.set_ylim(bottom=0.6, top=1)
    '''
    ax.text(68, 0.93, waves[i] + ' $\mathrm{\AA{}}$', ha='right')
    ax.minorticks_on()
    ax.tick_params(axis='both', which='minor', direction='in', length=4)
    ax.tick_params(axis='both', which='major', direction='in', length=6)
    #ax.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    #ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    #ax.set_yticklabels((np.arange(ax.get_ylim()[0], ax.get_ylim()[1]+0.1, 0.1)))
    '''
    majorLocator = mtick.LinearLocator(numticks=10)
    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(minorLocator)
    ax.set_xticks(np.arange(0,80,10), minor=True)
    ax.set_xticklabels(fontsize=12)
    ax.set_yticklabels(np.arange(0,1,0.1),fontsize=12)
    '''

fig.text(0.5, 0.024, 'radius [pixels]', ha='center', fontsize=fontsize)
fig.text(0.03, 0.5, 'maximum cross-correlation', va='center', rotation='vertical', fontsize=fontsize)
fig.subplots_adjust(left=0.1, right=0.85, bottom=0.08, top=0.95, wspace=0.2, hspace=0.2)
cax = fig.add_axes([0.90, 0.05, 0.02, 0.90])
#step=30
cbar = fig.colorbar(m, cax=cax)
cbar.set_label('timelag [image, with cadence = 12 s]', rotation=270)
#cbar.set_ticks(np.arange(min(t),max(t)+step,step))
#cbar.set_ticklabels(np.arange(min(t),max(t)+step,0.5*step))
#cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar

plt.show(block=False)
#plt.savefig('bp_size1.png', bbox_inches='tight', dpi=300)
#plt.savefig('bp_size2.png', bbox_inches='tight', dpi=300)
