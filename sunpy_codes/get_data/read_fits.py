'''
Programmer:     Laurel Farris
Last modified:  27 June 2016

This should be modified with a keyword set to true or false, specifying
whether the exact file names are entered. If they are, the 'glob.glob'
part can be skipped.
'''
from astropy.io import fits
import glob
# import pdb


def read_fits(data_path):
    '''
    Read fits data and return it as a list object that contains
    both the headers and the data.
    '''
    fls = glob.glob(data_path + "*.fits")
    hdu = []
    for f in fls:
        datum = fits.open(f)
        hdu.append(datum[0])  # PrimaryHDU ([0])
        datum.close()
    return hdu

hdu = read_fits("/Users/laurel/sunpy/data/sample_data/")
