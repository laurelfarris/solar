# from read_fits import read_fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

f = "/Users/laurel/sunpy/data/aia.fits"
hdu = fits.open(f)
header = hdu[0].header
data = hdu[0].data
im = np.power(data, 0.5)
hdu.close()



fig = plt.figure()
ax = fig.add_subplot(111)

ax.imshow(im, cmap='gray')
plt.colorbar()

# ax.set_ymargin(0.5) # Can't tell what this does
ax.set_xlabel("x [pixels]")
ax.set_ylabel("y [pixels]")

# Turn on minor tick marks
ax.minorticks_on()

# Axis limits
start, end = ax.get_xlim()
chop = 400
start = int(start + chop) + 1
end = int(end - chop) + 1
ax.set_xlim([start, end])
ax.set_ylim([start, end])

# Density of (minor) ticks. List of ticks is only input
t = ax.get_xticks(minor=True)
ax.set_xticks(np.arange(min(t),max(t),len(t)*2), minor=True)
ax.set_yticks(np.arange(min(t),max(t),len(t)*2), minor=True)



# Appearence of ticks... lots of kwargs!!
ax.tick_params(
  which='minor',
  length=5
)
ax.tick_params(
  which='major',
  length=10,
  width=1.2,
)
ax.tick_params(
  which='both',
  direction='out',
  labelsize=10, # numbers (TICK label, not axis label)
  #pad=10,
  #width=2,
)

'''
# Set scientific notation
ax.ticklabel_format(
  axis='both',
  scilimits=(0,0)
)
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
'''
plt.show()
'''
'''


