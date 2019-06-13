## Copyright (C) 2019 SuperDARN
# Authors: Marina Schmidt and Danno Peters

"""
This module contains SuperDARN radar information
"""
from typing import NamedTuple
from enum import Enum

"""
_Hemispheres Class - Used to denote which hemisphere a radar is located in
      _Hemisphere.North = 1
      _Hemisphere.South = 0
"""
class _Hemisphere(Enum):
    North = 0
    South = 1

"""
_Coord Class - Used to store Geo Coordinates (utilized for both GeoGraphic and GeoMagnetic)
      Nested inside of _Radar Named Tuple, composed of three floats representing location and boresight direction

      lat: Latitude in decimal format
      lon: Longitude in decimal format
      bore: Boresight in decimal format
"""
class _Coord(NamedTuple):
  lat: float
  lon: float
  bore: float

"""
_Radar Class - Used to store relevent information about the SuperDARN Radars
      Nested inside of _Radar Named Tuple, composed of three floats representing location and boresight direction
      
      name: full text of radar name
      stid: station number
      acronym: three letter station acronym
      beams: number of possible beams
      gates: number of range gates per beam
      geographic: Named Tuple containing geographic latitude longitude and boresight
      geomagnetic: Named Tuple containing geomagnetic latitude longitude and boresight
      hemisphere: _Hemisphere
      institute: full text name of institution operating the radar site
"""
class _Radar(NamedTuple):
    name: str
    stid: int
    acronym: str
    beams: int
    gates: int
    geographic: _Coord
    geomagnetic: _Coord
    hemisphere: _Hemisphere
    institute: str

"""
SuperDARNRadars Class - contains a dictionary of Nested Named Tuples with information about each radar
    Dictioanry index is the radar station ID number
    
    Accessed using SuperDARNRadars.radar[**StationID**].**Tuple Name**
        Where:  
                **StationID** is an integer station ID, ie 5
                **Tuple Name** is the name of a tuple, ie institute 

        Example:
                SuperDARNRadars.radar[5].institute retuns the string "University of Saskatchewan"
"""
class SuperDARNRadars():
    # Information obtained from http://vt.superdarn.org/tiki-index.php?page=Radar+Overview
    radars = {209: _Radar( 'Adak Island East',       209, 'ade', 22, 110, _Coord(51.88, -176.63, 46.0),     _Coord(47.6, -113.0, 31.6),     _Hemisphere.North, 'University of Alaska'),
              208: _Radar( 'Adak Island West',       208, 'adw', 22, 110, _Coord(51.88, -176.63, -28.0),    _Coord(47.6, -113.0, -34.2),    _Hemisphere.North, 'University of Alaska'),
              33: _Radar( 'Blackstone',              33,  'bks', 24, 110, _Coord(37.10, -77.95, -40.0),     _Coord(48.2, -2.7, -41.5),      _Hemisphere.North, 'Virginia Tech'),
              24: _Radar( 'Buckland Park',           24,  'bpk', 16, 110, _Coord(-34.620,  138.460, 146.5), _Coord(-46.2,  -146.1, None),   _Hemisphere.South, 'La Trobe University'),
              207: _Radar( 'Christmas Valley East',  207, 'cve', 24, 75,  _Coord(43.27, -120.36, 54.0),     _Coord(49.5, -58.3, 40.2),      _Hemisphere.North, 'Dartmouth College'),
              206: _Radar( 'Christmas Valley West',  206, 'cvw', 22, 75,  _Coord(43.27, -120.36, -20.0),    _Coord(49.5, -58.3, -31.2),     _Hemisphere.North, 'Dartmouth College'),
              66: _Radar( 'Clyde River',             66,  'cly', 16, 100, _Coord(70.49, -68.50, -55.6),     _Coord(78.8, 18.1, -42.5),      _Hemisphere.North, 'University of Saskatchewan'),
              96: _Radar( 'Dome C',                  96,  'dce', 22, 75,  _Coord(-75.090,  123.350, 115.0), _Coord(-88.9,  54.6,  -105.5),  _Hemisphere.South, 'Institute for Space Astrophysics and Planetology'),
              21: _Radar( 'Falkland Islands',        21,  'fir', 16, 75,  _Coord(-51.83, -58.98,  178.2),   _Coord(-39.0,  9.9, 172.4),     _Hemisphere.South, 'British Antarctic Survey'),
              205: _Radar( 'Fort Hays East',         205, 'fhe', 22, 110, _Coord(38.86, -99.39, 45.0),      _Coord(48.9, -32.2, 41.3),      _Hemisphere.North, 'Virginia Tech'),
              204: _Radar( 'Fort Hays West',         204, 'fhw', 22, 110, _Coord(38.86, -99.39, -25.0),     _Coord(48.9, -32.2, -32.3),     _Hemisphere.North, 'Virginia Tech'),
              1: _Radar( 'Goose Bay',                1,   'gbr', 16, 100, _Coord(53.32,  -60.46,  5.0),     _Coord(61.1, 22.9,  11.0),      _Hemisphere.North, 'Virginia Tech'),
              4: _Radar( 'Halley',                   4,   'hal', 16, 75,  _Coord(-75.52, -26.63,  165.0),   _Coord(-62.1,  29.3,  174.1),   _Hemisphere.South, 'British Antarctic Survey'),
              10: _Radar( 'Hankasalmi',              10,  'han', 16, 75,  _Coord(62.32,  26.61, -12.0),     _Coord(59.1, 104.5, 1.5),       _Hemisphere.North, 'University of Leicester'),
              40: _Radar( 'Hokkaido East',           40,  'hok', 16, 110, _Coord(43.53,  143.61,  25.0),    _Coord(37.3,  -144.9,  23.9),   _Hemisphere.North, 'Nagoya University'),
              41: _Radar( 'Hokkaido West',           41,  'hkw', 16, 110, _Coord(43.54,  143.61,  -30.0),   _Coord(37.3, -144.9, None),     _Hemisphere.North, 'Nagoya University'),
              64: _Radar( 'Inuvik',                  64,  'inv', 16, 100, _Coord(68.414, -133.772,  26.4),  _Coord(71.5,  -85.1, 4.4),      _Hemisphere.North, 'University of Saskatchewan'),
              3: _Radar( 'Kapuskasing',              3,   'kap', 16, 100, _Coord(49.39,  -82.32,  12.0),    _Coord(60.2,  -8.3,  15.3),     _Hemisphere.North, 'Virginia Tech'),
              15: _Radar( 'Kergueien',               15,  'ker', 16, 75,  _Coord(-49.22, 70.14, 168.0),     _Coord(-58.7,  122.7, -163.0),  _Hemisphere.South, 'IRAP/CNRS/IPEV'),
              16: _Radar( 'King Salmon',             16,  'ksr', 16, 75,  _Coord(58.68,  -156.65, -20.0),   _Coord(57.5, -99.1, -31.3),     _Hemisphere.North, 'National Institute of Information and Communication'),
              7: _Radar( 'Kodiak',                   7,   'kod', 16, 75,  _Coord(57.62,  -152.19, 30.0),    _Coord(57.2,  -94.9, 11.9),     _Hemisphere.North, 'University of Alaska'),
              90: _Radar( 'Longyearbyen',            90,  'lyr', 16, 110, _Coord(78.153, 16.074,  23.7),    _Coord(74.87, 127.67, None),    _Hemisphere.North, 'University Centre in Svalbard'),
              20: _Radar( 'McMurdo',                 20,  'mcm', 16, 75,  _Coord(-77.88, 166.73,  300.0),   _Coord(-80.0,  -33.3, -148.2),  _Hemisphere.South, 'University of Alaska, Fairbanks'),
              6: _Radar( 'Prince George',            6,   'pgr', 16, 75,  _Coord(53.98,  -122.59, -5.0),    _Coord(59.6,  -64.3, -16.2),    _Hemisphere.North, 'University of Saskatchewan'),
              9: _Radar( 'Pykkvibaer',               9,   'pyk', 16, 75,  _Coord(63.77, -20.54,  30.0),     _Coord(64.6, 67.3,  40.2),      _Hemisphere.North, 'University of Leicester'),
              65: _Radar( 'Rankin Inlet',            65,  'rkn', 16, 100, _Coord(59.6, -64.3, -16.2),       _Coord(72.6, -26.4, 1.8),       _Hemisphere.North, 'University of Saskatchewan'),
              11: _Radar( 'SANAE',                   11,  'san', 16, 75,  _Coord(-71.68, -2.85, 173.2),     _Coord(-61.8,  43.7,  -162.4),  _Hemisphere.South, 'South Africa National Space Agency'),
              5: _Radar( 'Saskatoon',                5,   'sas', 16, 75,  _Coord(52.16,  -106.53, 23.1),    _Coord(60.9,  -43.8, 16.9),     _Hemisphere.North, 'University of Saskatchewan'),
              2: _Radar( 'Schefferville',            2,   'sch', 16, 75,  _Coord(54.80,  -66.80,  15.0),    _Coord(63.7,  14.9,  21.9),     _Hemisphere.North, 'CNRS/LPCE'),
              22: _Radar( 'South Pole Station',      22,  'sps', 16, 75,  _Coord(-89.995,  118.291, 75.7),  _Coord(-74.3, 18.5,  -20.3),    _Hemisphere.South, 'University of Alaska, Fairbanks'),
              8: _Radar( 'Stokkseyri',               8,   'sto', 16, 75,  _Coord(63.86,  -21.031, -59.0),   _Coord(64.9, 66.1,  -33.0),     _Hemisphere.North, 'Lancaster University'),
              13: _Radar( 'Syowa East',              13,  'sye', 16, 75,  _Coord(-69.00, 39.58, 106.5),     _Coord(-66.5,  72.2,  143.0),   _Hemisphere.South, 'National Institute of Polar Research'),
              12: _Radar( 'Syowa South',             12,  'sys', 16, 75,  _Coord(-69.00, 39.58, 159.0),     _Coord(-66.5,  72.2,  -157.7),  _Hemisphere.South, 'National Institute of Polar Research'),
              14: _Radar( 'Tiger',                   14,  'tig', 16, 75,  _Coord(-43.40, 147.20,  180.0),   _Coord(-54.8,  -133.2,  169.4), _Hemisphere.South, 'La Trobe University'),
              18: _Radar( 'Unwin',                   18,  'unw', 16, 75,  _Coord(-46.51, 168.38,  227.9),   _Coord(-54.4,  -106.2,  -152.2),_Hemisphere.South, 'La Trobe University'),
              32: _Radar( 'Wallops Island',          32,  'wal', 24, 110, _Coord(37.93,  -75.47,  35.9),    _Coord(48.7,  0.8, 46.7),       _Hemisphere.North, 'JHU Applied Physics Laboratory'),
              19: _Radar( 'Zhongshan',               19,  'zho', 16, 75,  _Coord(-69.38, 76.38, 72.5),      _Coord(-74.9, 97.2,  123.5),    _Hemisphere.South, 'Polar Research Institute of China')}