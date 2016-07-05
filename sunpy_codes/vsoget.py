'''
Programmer:     Laurel Farris
Last modified:  27 June 2016

'''
from sunpy.net import vso
from sunpy.time import parse_time
import astropy.units as u
import pdb

'''
This code was constructed using the syntax provided by
SunPy.org, modelled after vsoget.pro from Sam.
Download data. If you have set your default download directory in your
sunpyrc configuration file then you do not need to identify a path at all.
Add '.wait()' at the end to keep the script from continuing until the
data has been downloaded (if needed).
'''

# def VSOsearch():
''' Create a new VSOClient instance and specify attributes '''
client = vso.VSOClient()

tstart = parse_time('2012/06/01 01:00:00')
tend = parse_time('2012/06/01 01:59:59')
inst = 'aia'
wave_min = 193
wave_max = 193
# sample = '12'  # Cadence desired (in seconds).

my_query = client.query(
  vso.attrs.Time(tstart, tend),
  vso.attrs.Instrument(inst),
  vso.attrs.Wave(wave_min*u.AA, wave_max*u.AA)
)

''' Print the number of matches '''
print ("Number of records found: {}".format(len(my_query)))
pdb.set_trace()

# def VSOget():
res = client.get(my_query, path="/Users/laurel/sunpy/data/{instrument}/{file}.fits")
