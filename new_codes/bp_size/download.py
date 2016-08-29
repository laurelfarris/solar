'''
This is just an outline for now.
It did not download readable data for whatever reason,
so my data was downloaded with the corresponding IDL code.
'''

from Modules import VSOsearch
from Modules import VSOget
import pdb
import numpy as np
import matplotlib.pyplot as plt
from get_data import read_fits


def my_download():
    my_client = vso.VSOClient()

    ''' Query the VSO. Input wavelength(s) as a list '''
    tstart = '2012/06/01 01:00:00'
    tend = '2012/06/01 01:00:59'
    inst = 'aia'
    my_wave = [94,131,171,211,304,335]
    my_sample = 12
    my_query = VSOsearch(my_client, tstart, tend, inst, wave=my_wave, sample=my_sample)

    ''' Download data from the VSO '''
    path1 = '/Users/laurel/sunpy/data/{instrument}/{file}.fits'
    path2 = "/solarstorm/laurel07/data/AIA/"
    my_data = VSOget(my_client, my_query, path2)


def read_my_fits():
    ''' Needs to return multiple data cubes for every wavelength.
        Get dictionary with headers and data '''
    path = "/solarstorm/laurel07/data/AIA/"
    waves = [94, 131, 171, 193, 211, 304, 335]
    for w in waves:
        hdu = read_fits(path + "*" + str(w) + "A_2012*.fits")
        data = np.stack(hdu['data'], axis=2)
        data = np.where(data >= 0, data, np.zeros(data.shape))

def save_my_data(cube, path):
    ''' Use python's numpy.save function to save data '''
    print "Start saving: " + str(datetime.now())
    np.save(path, cube)
    print "Finished saving: " + str(datetime.now())
    return 0
