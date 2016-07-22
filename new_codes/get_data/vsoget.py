'''
Programmer:     Laurel Farris
Last modified:  20 July 2012

'''
from sunpy.net import vso
from sunpy.time import parse_time
import astropy.units as u
import pdb
import sys
#pdb.set_trace()

'''
This code was constructed using the syntax provided by SunPy.org,
modelled after vsoget.pro provided by Sam (author?)
Download data. If you have set your default download directory in your
sunpyrc configuration file then you do not need to identify a path at all.
Add '.wait()' at the end to keep the script from continuing until the
data has been downloaded (if needed).
'''

def VSOsearch(client, tstart, tend, inst,
              wave=[94,131,171,193,211,304,335],
              sample=12):

    ''' Take string arg and return a datetime object '''
    tstart = parse_time(tstart)
    tend = parse_time(tend)

    ''' Specify wavelength(s), query for all if none specified by user '''
    if (inst!='aia'):
        sys.exit("Not ready for other instruments. Sorry.")

    ''' Return a LIST of response objects, each of which is a record found by the VSO '''
    qr = []  # Should make this a dictionary!
    for w in wave:
        qr.append(client.query(
          vso.attrs.Time(tstart, tend),
          vso.attrs.Instrument(inst),
          vso.attrs.Wave(w*u.AA, w*u.AA),
          vso.attrs.Sample(sample*u.second)
          )
        )

    ''' Print the number of matches '''
    #print ("Number of records found: {}".format(len(qr)))
    return qr


def VSOget(client, qr, path):
    for lis in qr:
        data = client.get(lis, path).wait()


''' Create a new VSOClient instance. This handles the particulars of how the data
from the data provider is downloaded to your computer. '''
my_client = vso.VSOClient()

''' Query the VSO. Input wavelength(s) as a list '''
tstart = '2012/06/01 01:00:00'
tend = '2012/06/01 01:00:59'
inst = 'aia'
my_wave = [193]
my_sample = 12
my_query = VSOsearch(my_client, tstart, tend, inst, wave=my_wave, sample=my_sample)

''' Download data from the VSO '''
path = '~/sunpy/data/{instrument}/{file}.fits'
my_data = VSOget(my_client, my_query, path)
