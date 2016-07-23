from sunpy.net import vso
from vsoget import VSOsearch
from vsoget import VSOget
from vsoget import read_fits

''' Create a new VSOClient instance. This handles the particulars of how the data
    from the data provider is downloaded to your computer. '''
my_client = vso.VSOClient()

''' Query the VSO. Input wavelength(s) as a list '''
tstart = '2012/06/01 01:00:00'
tend = '2012/06/01 01:00:59'
inst = 'aia'
#my_wave = [94,131,171,211,304,335]
my_wave = [94,131]
my_sample = 12
my_query = VSOsearch(my_client, tstart, tend, inst, wave=my_wave, sample=my_sample)
#pdb.set_trace()

''' Download data from the VSO '''
path = '/Users/laurel/sunpy/data/{instrument}/{file}.fits'
path2 = "/solarstorm/laurel07/data/AIA/"
#my_data = VSOget(my_client, my_query, path)
#pdb.set_trace()

''' Read fits and (if desired) pickle returned object
    (this process takes a long time, so probably good idea to save the data) '''
#hdu = read_fits(path)  #, "aia193hdu.p")
#pdb.set_trace()
