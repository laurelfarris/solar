from vsoget import read_fits

path = "/solarstorm/laurel07/data/AIA/"
hdu_94 = read_fits(path + "*94*.fits")

# Make a data cube (one wavelength only, for now)
x = (hdu_94['data'][0].shape[1])
y = (hdu_94['data'][0].shape[0])
z = len(hdu['data'])
data_94 = np.zeros((x, y, z))
for i in range(1, z):
    np.append(data_94, np.expand_dims(hdu['data'][i], axis=2), axis=2)

''' data_94 is the data cube for lambda = 94 Angstroms '''


''' Align data (make a module... github?) '''


''' Save portion of data with bright point (BP) only '''

BP = data[x1:x2, y1:y2, :]

''' Save data to file '''





hdu_131 = read_fits(path + "*131*.fits")
hdu_171 = read_fits(path + "*171*.fits")
hdu_193 = read_fits(path + "*193*.fits")
hdu_211 = read_fits(path + "*211*.fits")
hdu_304 = read_fits(path + "*304*.fits")
hdu_335 = read_fits(path + "*335*.fits")
