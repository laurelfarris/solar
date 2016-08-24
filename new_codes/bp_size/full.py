'''
Programmer:         Laurel Farris
Last modified:      13 August 2016
'''
import pdb
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import sunpy
import sunpy.map
import sunpy.cm
import matplotlib.colors as colors
from sunpy.net import vso
from sunpy.time import parse_time
from astropy.io import fits
import astropy.units as u
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
x0 = -550 * u.arcsecond
y0 = 350 * u.arcsecond
length = 50 * u.arcsecond
#header=[] data=[] fls=[]
    #hdu = fits.open((glob.glob(path + "*" + waves[i] + "A_2012*.fits"))[0])
    #header.append(hdu[0].header) #data.append(hdu[0].data)
    #header = hdu[0].header data = hdu[0].data
    #hdu.close()
#path = '/solarstorm/laurel07/data/AIA/'
path = '/Users/laurel/sunpy/data/AIA/'
waves = ['94', '131', '171', '193', '211', '304', '335']

fig = plt.figure(figsize=(9,6))

'''
fls = glob.glob(path + '*193A_2012*.fits')
m = sunpy.map.Map(fls[0])
m = m.submap(
  u.Quantity([x0 - length, x0 + length]),
  u.Quantity([y0 - length, y0 + length]))
ax = fig.add_subplot(1,1,1,projection = m)
cmap1=plt.cm.Greys_r
cmap2=plt.get_cmap('sdoaia193'),
m.plot(annotate=False, cmap=cmap1,
      norm=colors.LogNorm())
plt.show(block=False)

'''
for i in range(0, len(waves)-1):
    fls = glob.glob(path + '*' + waves[i] + 'A_2012*.fits')
    m = sunpy.map.Map(fls[0])
    m = m.submap(
      u.Quantity([x0 - length, x0 + length]),
      u.Quantity([y0 - length, y0 + length]))
    ax = fig.add_subplot(2,3,i+1,projection = m)
    #m.plot_settings['title'] = m.detector
    #m.plot_settings['x_title'] = ' ' #'AIA/SDO ' + waves[i]
    m.plot(annotate=False, cmap=plt.get_cmap('sdoaia'+waves[i]),
   #       norm=colors.LogNorm(
    #        vmin=0, vmax=m.max())
            #vmin=max(0,m.min()), vmax=m.max())
          )
    #m.draw_rectangle(bottom_left=u.Quantity([x0-length, y0-length]), width=u.Quantity(length*2), height=u.Quantity(length*2))


    lon = ax.coords[0]  # x
    lat = ax.coords[1]  # y
    lon.set_ticklabel_visible(False)
    lon.set_ticks_visible(False)
    lon.set_axislabel('')
    lat.set_ticklabel_visible(False)
    lat.set_ticks_visible(False)
    lat.set_axislabel('')

    # Prevent the image from being re-scaled while overplotting.
    #ax.set_autoscale_on(False)
    #xc = [0,100,1000] * u.arcsec
    #yc = [0,100,1000] * u.arcsec

    # ax.get_transform() tells WCSAxes what coordinates to plot in.
    # 'world' coordinates are always in degrees
    #p = plt.plot(xc.to(u.deg), yc.to(u.deg), 'o', transform=ax.get_transform('world'))


    ax.axis('tight')
    ax.text(0.8, 0.9, waves[i] + '$\mathrm{\mathbf{\AA{}}}$', fontweight='bold', fontsize=10, transform=ax.transAxes)

#plt.subplots_adjust(wspace=0.1, hspace=0.1)
#fig.tight_layout()
#plt.show(block=False)
#plt.colorbar()
plt.savefig('full_bp.png', bbox_inches='tight', dpi=300)
