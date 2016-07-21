'''
Programmer:     Laurel Farris
Last modified:  20 July 2012

'''
from sunpy.net import vso
from sunpy.time import parse_time
import astropy.units as u
import pdb

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

    ''' Specify instrument, wavelength(s), and cadence (seconds) '''
    inst = inst
    if not wave:
        
    
    wave_min = wave
    wave_max = wave
    # sample = '12'

    ''' Print the number of matches '''
    print ("Number of records found: {}".format(len(my_query)))
    #pdb.set_trace()

    ''' Return a LIST of response objects, each of which is a record found by the VSO '''
    return client.query(
      vso.attrs.Time(tstart, tend),
      vso.attrs.Instrument(inst),
      vso.attrs.Wave(wave_min*u.AA, wave_max*u.AA)
      )

def VSOget():
    #res = client.get(my_query, path="/Users/laurel/sunpy/data/{instrument}/{file}.fits")
    return 0



my_query = VSOsearch('2012/06/01 01:00:00','2012/06/01 01:00:59', 'aia')




