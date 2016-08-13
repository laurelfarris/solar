'''
Programmer:         Laurel Farris
Last modified:      12 August 2016
'''
import pdb
import numpy as np
import matplotlib.pyplot as plt
import sunpy
import sunpy.map
import sunpy.cm
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

path = "/solarstorm/laurel07/data/AIA/"
waves = ['94', '131', '171', '193', '211', '304', '335']

# fig, ax = plt.subplots(figsize=(9,6), nrows=2, ncols=3, sharex=True, sharey=True)
fig, ax = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True)
axes = [ax[0,0],ax[0,1],ax[0,2],ax[1,0],ax[1,1],ax[1,2]]

#x = 1140 & y = 2630 & radius = 50

for i in range(0, len(waves)-1):
    print i
    fls = glob.glob(path + "*" + waves[i] + "A_2012*.fits")
    hdu = fits.open(fls[0])
    header = hdu[0].header
    data = hdu[0].data
    hdu.close()
    
    wavelength = header['wavelnth']
    axes[i] = sunpy.map.Map(fls[0])
    
    #axes[i] = sunpy.map.Map((data[x-radius:x+radius, y-radius:y+radius], header))
    axes[i].plot_settings['title'] = '' #'AIA/SDO ' + str(wavelength)
    axes[i].plot_settings['cmap'] = plt.get_cmap('sdoaia' + str(wavelength))

    axes[i].plot()
    plt.show(block=False)
    pdb.set_trace()

#plt.colorbar()
#plt.show(block=False)
'''
'''
