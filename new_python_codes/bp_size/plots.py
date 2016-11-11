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

fig = plt.figure(figsize=(10,8))
fontsize=12
waves = ['94', '131', '171', '193', '211', '304'] #, '335']
x = [0.10, 0.35, 0.65, 0.10, 0.35, 0.65]
y = [0.10, 0.10, 0.10, 0.45, 0.45, 0.45]

for i in range(0, len(waves)):
    f = open(waves[i] + '_bp_sizes.dat')
    x, y, r, cor, t = np.loadtxt(f, unpack=True)
    '''
    r = r*0.6
    r = r.astype(float)
    '''

    ax = fig.add_subplot(2,3,i+1)
    m = ax.scatter(r, cor, c=t, vmin=min(t), vmax=max(t), cmap='viridis', s=4, lw=0)
    #m = ax.scatter(r, cor, c=t, vmin=-50, vmax=50, cmap='viridis', s=4, lw=0)
    #ax.axis('tight')
    ax.set_xlim(left=0, right=0.5*max(r))
    ax.set_ylim(bottom=0.5, top=1)
    ax.set_aspect(70./1.)
    '''
    '''
    ax.text(0.9, 0.9, waves[i] + ' $\mathrm{\AA{}}$', ha='center', transform=ax.transAxes )
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

fig.text(0.5, 0.024, 'radius [pixels] (1 pixel = 0.6")', ha='center', fontsize=fontsize)
fig.text(0.03, 0.5, 'maximum cross-correlation', va='center', rotation='vertical', fontsize=fontsize)

#fig.subplots_adjust(left=0.1, right=0.95, bottom=0.08, top=0.75, wspace=0.1, hspace=0.1)
fig.subplots_adjust(bottom=0.1, top=0.75)

''' color bar '''
cax = fig.add_axes([0.1, 0.90, 0.80, 0.03])
cbar = fig.colorbar(m, cax=cax, orientation='horizontal')
cbar.set_label('timelag [image, with cadence = 12 s]', style='italic', va='top')
#cbar.set_ticks(np.arange(min(t),max(t)+step,step))
#cbar.set_ticklabels(np.arange(min(t),max(t)+step,0.5*step))
#cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar

#plt.show(block=False)
plt.savefig('figure_4.png', bbox_inches='tight', dpi=300)
#plt.savefig('bp_size2.png', bbox_inches='tight', dpi=300)
