'''
Programmer:     Laurel Farris
Last modified:  20 July 2012

'''
from sunpy.net import vso
from sunpy.time import parse_time
import astropy.units as u
import pdb
#pdb.set_trace()

'''
This code was constructed using the syntax provided by SunPy.org,
modelled after vsoget.pro provided by Sam (author?)
Download data. If you have set your default download directory in your
sunpyrc configuration file then you do not need to identify a path at all.
Add '.wait()' at the end to keep the script from continuing until the
data has been downloaded (if needed).
'''

def VSOsearch(tstart, tend, inst, wave=None):

    ''' Create a new VSOClient instance. This handles the particulars of how the data
    from the data provider is downloaded to your computer. '''
    client = vso.VSOClient()

    ''' Take string arg and return a datetime object '''
    tstart = parse_time('2012/06/01 01:00:00')
    tend = parse_time('2012/06/01 01:59:59')

    ''' Instrument ''' 
    inst = inst

    ''' Sample (cadence) '''
    sample = 60

    ''' Specify wavelength(s), query for all if none specified by user '''
    if (inst=='aia'):
        if not wave:
            wave = [94,131,171,193,211,304,335]
        else:
            wave = [wave]

    ''' Return a LIST of response objects, each of which is a record found by the VSO '''
    qr = []  # Should make this a dictionary!
    for w in wave:
        qr.append(client.query(
          vso.attrs.Time(tstart, tend),
          vso.attrs.Instrument(inst),
          vso.attrs.Wave(w*u.AA, w*u.AA)
          ))

    ''' Print the number of matches '''
    #print ("Number of records found: {}".format(len(qr)))
    return qr

def VSOget(qr, path):
    client = vso.VSOClient()
    return client.get(qr, path)

path = "~/sunpy/data/{instrument}/{file}.fits"
my_query = VSOsearch('2012/06/01 01:00:00','2012/06/01 01:00:59', 'aia', 193)
my_data = VSOget(my_query, path)
