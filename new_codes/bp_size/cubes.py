import pdb
import numpy as np
import matplotlib.pyplot as plt
from get_data import read_fits


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
    print "Start saving: " + str(datetime.now())
    np.save(path, cube)
    print "Finished saving: " + str(datetime.now())
    return 0
