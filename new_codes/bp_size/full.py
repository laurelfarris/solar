'''
Programmer:         Laurel Farris
Last modified:      13 August 2016
'''
import pdb
import sys
import numpy as np
import matplotlib.pyplot as plt
import sunpy
import sunpy.map
import sunpy.cm
import matplotlib.colors as colors
from sunpy.net import vso
from sunpy.time import parse_time
from astropy.io import fits
import glob
#import get_data


def read_my_fits():
    ''' returns data cube with negative values set to zero '''
    path = "/solarstorm/laurel07/data/AIA/"
    waves = [94, 131, 171, 193, 211, 304, 335]
    my_list = []
    for w in waves:
        fls = glob.glob(path + "*" + str(w) + "A_2012*.fits")
        my_list.append(fls[0])
    my_hdu = get_data.read_fits(my_list)
    return my_hdu


def make_cube(my_hdu):
    data = np.stack(my_hdu['data'], axis=2)
    data = np.where(data >= 0, data, np.zeros(data.shape))
    return data


    w, h = 10, 8
    fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(w,h))
    x = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]

    for i in range(len(x)):
        ax[x[i]].imshow(np.power(data[:,:,i], 0.5), cmap='gray')
        ax[x[i]].set_xticklabels([])
        ax[x[i]].set_yticklabels([])

    #fig.tight_layout()
    #fig.subplots_adjust(wspace=0, hspace=0)
    plt.subplots_adjust(left=1/w, right=1-1/w, bottom=1/h, top=1-1/h)
    plt.show(block=False)
    #return fig, ax


''' Make panel of multi-wavelength images of bright point '''

#path = "/solarstorm/laurel07/data/AIA/"
path = "~/sunpy/data/AIA/"
waves = ['94', '131', '171', '193', '211', '304', '335']

#fig, ax = plt.subplots(figsize=(9,6),nrows=2, ncols=3)
    #gridspec_kw={'width_ratios':[1,1,1,1,1]}, # 'height_ratios':[1,1]},
    #sharex=True, sharey=True
fig = plt.figure()

#x = 1140 & y = 2630 & radius = 50
#axes[i] = sunpy.map.Map((data[x-radius:x+radius, y-radius:y+radius], header))

#header=[] data=[] fls=[]
for i in range(0, len(waves)-1):
    #hdu = fits.open((glob.glob(path + "*" + waves[i] + "A_2012*.fits"))[0])
    #header.append(hdu[0].header) #data.append(hdu[0].data)
    #header = hdu[0].header data = hdu[0].data
    #hdu.close()
    ax = fig.add_subplot(2,3,i+1)
    fls = glob.glob(path + "*" + waves[i] + "A_2012*.fits")
    m = sunpy.map.Map(fls[0])
    # m.index('unwanted x/y label')... should return key
    m.plot_settings['title'] = ' ' #'AIA/SDO ' + waves[i]
    m.plot_settings['x_title'] = ' ' #'AIA/SDO ' + waves[i]
    m.plot_settings['cmap'] = plt.get_cmap('sdoaia' + waves[i])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_xticks([])
    ax.set_yticks([])
    m.plot(xlabel='',ylabel='')
    #wavelength = header['wavelnth']
    '''
    #norm = colors.Normalize(vmin=0, vmaxes[i]=ax.mean() + 5 * axes[i].std())
    #axes[i].plot(norm=norm)
    '''


plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.show(block=False)
#plt.colorbar()
'''
'''
