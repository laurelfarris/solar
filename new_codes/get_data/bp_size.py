import pdb
import numpy as np
import matplotlib.pyplot as plt
from Modules import read_fits


path = "/solarstorm/laurel07/data/AIA/"
waves = [94, 131, 171, 193, 211, 304, 335]

''' Get dictionary with headers and data '''
#for w in waves:
#for i in range(0, len(waves)):
#hdu = read_fits(path + "*" + str(waves[i]) + "*.fits", num=1)

hdu_94 = read_fits(path + "*94*.fits", num=1)
hdu_131 = read_fits(path + "*131*.fits", num=1)
hdu_171 = read_fits(path + "*171*.fits", num=1)
hdu_193 = read_fits(path + "*193*.fits", num=1)
hdu_211 = read_fits(path + "*211*.fits", num=1)
hdu_304 = read_fits(path + "*304*.fits", num=1)
hdu_335 = read_fits(path + "*335*.fits", num=1)

''' Make a data cube (one wavelength only, for now) '''
data = np.stack(
    [hdu_94['data'][0],
    #hdu_131['data'][0],
    hdu_171['data'][0],
    hdu_193['data'][0],
    hdu_211['data'][0],
    hdu_304['data'][0],
    hdu_335['data'][0]],
    axis=2)

''' Image data '''
fig = plt.figure()
plt.ion()
for i in range(0, 6):
    ax = fig.add_subplot(2,3,i+1)
    ax.imshow(np.power(data[:,:,i], 1), cmap='gray')
    plt.draw()








''' Align data (make a module... github?) '''
''' Save portion of data with bright point (BP) only '''
#BP = data[x1:x2, y1:y2, :]
''' Save data to file '''
