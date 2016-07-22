'''
Programmer:     Laurel Farris
Last modified:  22 July 2012

'''
import pdb
import sys
from sunpy.net import vso
from sunpy.time import parse_time
import astropy.units as u
from datetime import datetime
from astropy.io import fits
import glob
import pickle

'''
This code was constructed using the syntax provided by SunPy.org,
modelled after vsoget.pro provided by Sam (author?)
Download data. If you have set your default download directory in your
sunpyrc configuration file then you do not need to identify a path at all.
'''

def VSOsearch(client, tstart, tend, inst,
              wave=[94,131,171,193,211,304,335],
              sample=12):

    ''' Specify wavelength(s), query for all if none specified by user '''
    if (inst!='aia'):
        sys.exit("Not ready for other instruments. Sorry.")

    ''' Return a LIST of response objects, each of which is a record found by the VSO '''
    wave = [94]
    qr = []
    for w in wave:
        qr.append(client.query(
          vso.attrs.Time(parse_time(tstart), parse_time(tend)),
          vso.attrs.Instrument(inst),
          vso.attrs.Wave(w*u.AA, w*u.AA),
          vso.attrs.Sample(sample*u.second)
          )
        )

    ''' Print the number of matches '''
    #print ("Number of records found: {}".format(len(qr)))
    return dict(zip(wave, qr))


def VSOget(client, qr, path):
    for lis in qr:
        data = client.get(lis, path).wait()


def read_fits(data_path, filename=None):
    '''
    Read fits data and returns the primary HDU,
    a list object that contains both the headers and the data.
    '''
    print "Start reading fits: " + str(datetime.now())
    fls = glob.glob(data_path + "*.fits")
    hdu = { 'data':[], 'header':[] }
    for f in fls:
        hdulist = fits.open(f)
        hdu['data'].append(hdulist[0].data)
        hdu['header'].append(hdulist[0].header)
        hdulist.close()
    print "Done: " + str(datetime.now())
    if filename:
        print "Start pickling: " + str(datetime.now())
        pickle.dump(hdu, open(filename, "wb"))
        print "Done pickling: " + str(datetime.now())
    return hdu


''' Create a new VSOClient instance. This handles the particulars of how the data
    from the data provider is downloaded to your computer. '''
my_client = vso.VSOClient()

''' Query the VSO. Input wavelength(s) as a list '''
tstart = '2012/06/01 01:00:00'

tend = '2012/06/01 01:00:59'
inst = 'aia'
my_wave = [94,131,171,211,304,335],
my_sample = 12
my_query = VSOsearch(my_client, tstart, tend, inst, wave=my_wave, sample=my_sample)
pdb.set_trace()

''' Download data from the VSO '''
path = '~/sunpy/data/{instrument}/{file}.fits'
my_data = VSOget(my_client, my_query, path)
pdb.set_trace()

''' Read fits and (if desired) pickle returned object
    (this process takes a long time, so probably good idea to save the data) '''
hdu_193 = read_fits("/solarstorm/laurel07/data/AIA/", "aia193hdu.p")
pdb.set_trace()

