import pdb
import numpy as np
import matplotlib.pyplot as plt
from Modules import read_fits
from sunpy.net import vso
from vsoget import VSOsearch
from vsoget import VSOget
from vsoget import read_fits

def my_download():
    ''' Create a new VSOClient instance. This handles the particulars of how the data
        from the data provider is downloaded to your computer. '''
    my_client = vso.VSOClient()

    ''' Query the VSO. Input wavelength(s) as a list '''
    tstart = '2012/06/01 01:00:00'
    tend = '2012/06/01 01:00:59'
    inst = 'aia'
    my_wave = [94,131,171,211,304,335]
    my_sample = 12
    #my_query = VSOsearch(my_client, tstart, tend, inst, wave=my_wave, sample=my_sample)

    ''' Download data from the VSO '''
    #path = '/Users/laurel/sunpy/data/{instrument}/{file}.fits'
    #path = "/solarstorm/laurel07/data/AIA/"
    #my_data = VSOget(my_client, my_query, path)

def read_my_fits():
    path = "/solarstorm/laurel07/data/AIA/"
    waves = [94, 131, 171, 193, 211, 304, 335]
    ''' Get dictionary with headers and data '''
    #for w in waves:
    #for i in range(0, len(waves)):
    #hdu = read_fits(path + "*" + str(waves[i]) + "*.fits", num=1)
    hdu_94 = read_fits(path + "*94A*.fits", num=1)
    hdu_131 = read_fits(path + "*131A*.fits", num=1)
    hdu_171 = read_fits(path + "*171A*.fits", num=1)
    hdu_193 = read_fits(path + "*193A*.fits", num=1)
    hdu_211 = read_fits(path + "*211A*.fits", num=1)
    hdu_304 = read_fits(path + "*304A*.fits", num=1)
    hdu_335 = read_fits(path + "*335A*.fits", num=1)
    ''' Make a data cube (one wavelength only, for now) '''
    data = np.stack(
        [hdu_94['data'][0],
        hdu_131['data'][0],
        hdu_171['data'][0],
        hdu_193['data'][0],
        hdu_211['data'][0],
        hdu_304['data'][0],
        hdu_335['data'][0]],
        axis=2)
    return data


def image_data(data):
    fig = plt.figure()
    plt.ion()
    for i in range(0, 6):
        ax = fig.add_subplot(2,3,i+1)
        ax.imshow(np.power(data[:,:,i], 1), cmap='gray')
    plt.draw()
    plt.show()


data = read_my_fits()



''' Align data (make a module... github?) '''
''' Save portion of data with bright point (BP) only '''
#BP = data[x1:x2, y1:y2, :]
''' Save data to file '''
