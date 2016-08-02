'''
This is just an outline for now.
It did not download readable data for whatever reason,
so my data was downloaded with the corresponding IDL code.
'''

from Modules import VSOsearch
from Modules import VSOget


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
    path = '/Users/laurel/sunpy/data/{instrument}/{file}.fits'
    path = "/solarstorm/laurel07/data/AIA/"
    my_data = VSOget(my_client, my_query, path)
