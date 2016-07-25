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
my_wave = [94,131,171,211,304,335]
my_sample = 12
#my_query = VSOsearch(my_client, tstart, tend, inst, wave=my_wave, sample=my_sample)

''' Download data from the VSO '''
#path = '/Users/laurel/sunpy/data/{instrument}/{file}.fits'
#path = "/solarstorm/laurel07/data/AIA/"
#my_data = VSOget(my_client, my_query, path)

''' Read fits and (if desired) pickle returned object
    (this process takes a long time, so probably good idea to save the data) '''

path = '/Users/laurel/sunpy/data/AIA/*94*.fits'
hdu = read_fits(path)  #, "aia193hdu.p")

# Make a data cube (one wavelength only, for now)
x = (hdu['data'][0].shape[1])
y = (hdu['data'][0].shape[0])
z = len(hdu['data'])
data_94 = np.zeros((x, y, z))
for i in range(1, z):
    np.append(data_94, np.expand_dims(hdu['data'][i], axis=2), axis=2)

# Align data (make a module... github?)


# Save portion of data with bright point (BP) only
BP = data[x1:x2, y1:y2, :]

# Save data to file
