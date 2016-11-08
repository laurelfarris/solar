import matplotlib.pyplot as plt
import numpy as np
import math
import pdb

import matplotlib
matplotlib.rc('font',**{'family':'serif','serif':['Times']})
matplotlib.rc('text', usetex=True)

''' Adjust size of figure window
from pylab import rcParams
width = 16
height = 5
rcParams['figure.figsize'] = width, height
'''

''' Open data file for plotting '''
f = open('radial_cc.dat')
x,y,xx,yy,r,c,t = np.loadtxt(f, unpack=True)
print np.amax(r)

''' Make a function to add subplots? and call in loop? '''

rows=1
cols=3
title = 'Central pixel: (' + str(int(x[0])) + ',' + str(int(y[0])) + ')'
x_lab = ['distance [pixels]','timelag [cadence (12 seconds)]','distance [pixels]']
y_lab = ['correlation','correlation','timelag [cadence (12 seconds)]']
colors = ['purple','green','blue','red']

fig = plt.figure()
fig.set_size_inches(15,4)
for i in range(0, rows*cols):
    ax = fig.add_subplot(rows,cols,i+1)
    #ax.set_title(title)
    ax.set_xlabel(x_lab[i])
    ax.set_ylabel(y_lab[i])
    ax.tick_params(axis='both',labelsize='small')

    for j in range(0,len(x)-1):
        ''' set color according to quadrant '''
        if xx[j] >= x[j] and yy[j] >= y[j]:
            color=colors[0]
        if xx[j] <= x[j] and yy[j] >= y[j]:
            color=colors[1]
        if xx[j] <= x[j] and yy[j] <= y[j]:
            color=colors[2]
        if xx[j] >= x[j] and yy[j] <= y[j]:
            color=colors[3]
        ''' break out when done with first bp '''
        if x[j+1] != x[j]:
            break
        ''' Create scatter plot '''
        if i == 0:
            ax.scatter(r[j],c[j],marker='.',s=2,color=color)
        if i == 1:
            ax.scatter(t[j],c[j],marker='.',s=2,color=color)
        if i == 2:
            ax.scatter(r[j],t[j],marker='.',s=2,color=color)
    ax.axis('tight')

#plt.show()
plt.savefig('test.png')





'''
# add another subplot for next bp

    if x[j+1] != x[j]:
        i=i+1
        ax = fig.add_subplot(2,2,i+1)
        ax.text(1.9,0.9,'('+str(int(x[j+1]))+','+str(int(y[j+1]))+')')
        ax.set_xlabel('distance [pixels]')
        ax.set_ylabel('correlation')
        ax.tick_params(axis='both',labelsize='small')
'''



'''
# Read in all data from a single file
i = 0
for line in f:
    if not line.startswith('#'):
        distance[i], cc[i] = np.loadtxt(f, unpack=True)
    else:
 Plots!
fig = plt.figure()
'''

'''
points = 4  # number of central pixels
for i in range(0,points):
    #f = open('interesting' + str(i+1) + '.dat')
    f = open('radial_cc.dat')
    x,y,xx,yy,r,c,t = np.loadtxt(f, unpack=True)
    ax = fig.add_subplot(2,2,i+1)
    ax.scatter(a,b,marker='.',s=2,color='purple')
    ax.tick_params(axis='both',labelsize='small')
    ax.set_xlabel('distance [pixels]')
    ax.set_ylabel('correlation')

i=0
ax = fig.add_subplot(2,2,i+1)

#plt.savefig('cc_distance.png',dpi=300)
#plt.savefig('cc_tau.png',dpi=300)
#plt.savefig('tau_distance.png',dpi=300)
'''

