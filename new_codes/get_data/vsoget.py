'''
Programmer:     Laurel Farris
Last modified:  22 July 2012
Purpose:        This code was constructed using the syntax provided by SunPy.org,
                modelled after vsoget.pro provided by Sam (author?)
                You can set a default download directory in your
                sunpyrc configuration file.
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


def VSOsearch(client, tstart, tend, inst,
              wave=[94,131,171,193,211,304,335],
              sample=12):

    ''' Specify wavelength(s), query for all if none specified by user '''
    if (inst!='aia'):
        sys.exit("Not ready for other instruments. Sorry.")

    ''' Return a LIST of response objects, each of which is a record found by the VSO '''
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

    ''' Return query as a dictionary. Access using qr[94], qr[131], etc. '''
    return dict(zip(wave, qr))


def VSOget(client, qr, path):
    for i in qr:
        data = client.get(qr[i], path).wait()


def read_fits(data_path)
    ''' Read fits data and returns the primary HDU,
        a list object that contains both the headers and the data. '''
    print "Start reading fits: " + str(datetime.now())
    fls = glob.glob(data_path)
    hdu = { 'data':[], 'header':[] }
    for f in fls:
        hdulist = fits.open(f)
        hdu['data'].append(hdulist[0].data)
        hdu['header'].append(hdulist[0].header)
        hdulist.close()
    print "Done: " + str(datetime.now())
    return hdu
