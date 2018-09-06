

import os
from datetime import datetime
from pydarn.io.cdmap import reader

class beamrecord():

    def __init__(self,scalardata,vectordata):
        self.scalardata = scalaradata
        self.vectordata = vectordata


class fitreader():

    def __init__(self,filename,reader_type='C',filetype='fitacf'):

        self.filename = filename
        self.fd = os.open(self.filename,os.O_RDONLY)
        self.fitfile = os.fdopen(self.fd)
        self.datarecords = []

        # TODO: get rid of while 1 and actually put a more meaningful condition in
        while 1:
            dfile = reader.read_dmap_rec(self.fd)
            # TODO: make this exception more menaingful
            if dfile == -1 :
                raise Exception("Error in reading {}".format(filename))
            # TODO: maybe create an object?
            if filetype == 'fitacf':
                scalardata = {'date': datetime(dfile['time.yr'],dfile['time.mo'],
                                               dfile['time.dy'],dfile['time.hr'],
                                               dfile['time.mt'],dfile['time.sc'],
                                               dfile['time.us'],UTC),
                              'radar version number': "{major}.{minor}"\
                              "".format(major=dfile['radar.revision.major'],
                                        minor=dflile['radar.revision.minor']),
                              'origin code': dfile[origin.code]
                              'origin time': datetime.strptime(dfile['origin.time'],
                                                               "%a %b %d %H:%M:%S %Y"),
                              'origin command': dfile['origin.command'],
                              'control program': dfile['cp'],
                              'station id': dfile['stid'],
                              'transmission power': dfile['txpow'], # kW
                              'num pulse seq transmitted': dfile['nave'],
                              'attenuation level': dfile['atten'],
                              'lag first range': dfile['lagfr'], # micro seconds
                              'sample seperation': dfile['smsep'], # micro seconds
                              'error code': dfile['ercod'],
                              'AGC': dfile['stat.agc'],
                              'LOPWR': dfile['stat.lopwr'],
                              'calc noise search': dfile['noise.search'],
                              'avg noise band': dfile['noise.mean'],
                              'channel': dfile['channel'],
                              'bmnum': dfile['dmnum'],
                              'bmazm': dfile['bmazm'],
                              'scan flag': dfile['scan'],
                              'channel offset': dfile['offset'],
                              'reciever rise': dfile['rxrise'], # microseconds
                              'integration': dfile['intt.sc']*1000000 + dfile['intt.us'], # microseconds
                              'tx pulse length': dfile['txpl'], # microseconds
                              'multipulse': dfile['mpinc'], # microseconds
                              'num pulses': dfile['mppul'],
                              'num lags': dfile['mplgs'],
                              'mplgexs': dfile['mplgexs'],
                              'ifmode': dfile['ifmode'],
                              'num ranges': dfile['nrang'],
                              'dist first range': dfile['frang'], # km
                              'range sep': dfile['rsep'], # km
                              'XCF flag': dfile['xcf'],
                              'trans freq': dfile['tfreq'],
                              'max pwr': dfile['mxpwr'], # kHz
                              'max noise level': dfile['lvmax'],
                              'comment buffer': dfile['combf'],
                              'fitacf version': "{major}.{minor}".format(major=dfile['fitacf.revision.major'],minor=dfile['fitacf.revision.minor']),
                              'sky noise': dfile['noise.sky'],
                              'lag0 noise ACF': dfile['noise.lag0'],
                              'vel noise ACF': dfile['noise.vel']}

                verctordata = {'pulse table': dfile['ptab'],
                               'lag table': dfile['ltab'],
                               'lag0 pwr': dfile['pwr0'],
                               'ranges': dfile['slist'],
                               'num points': dfile['nlag'],
                               'quality of fit ACF': dfile['qflag'],
                               'ground scatter flaf': dfile['gflg'],
                               'fit lambda pwr': dfile['p_l'],
                               'fit lambda error pwr': dfile['p_l_e'],
                               'sigma fit pwr': dfile['p_s'],
                               'sigma error fit pwr': dfile['p_s_e'],
                               'vel': dfile['v'],
                               'vel error': dfile['v_r'],
                               'lambda spectral width': dfile['w_l'],
                               'lambda spectral width error': dfile['w_l_e'],
                               'sigma spectral width': dfile['w_s'],
                               'sigma spectral width error': dfile['w_s_e'],
                               'std lambda': dfile['sd_l'],
                               'std sigma': dfile['sd_s'],
                               'std phi': dfile['sd_phi'],
                               'quality of fit': dfile['x_qflg'],
                               'ground scatter': dfile['x_gflg'],
                               'lambda pwr fit': dfile['x_p_l'],
                               'lambda pwr error': dfile['x_p_l_e'],
                               'sigma pwr fit': dfile['x_p_s'],
                               'vel XCF': dfile['x_v'],
                               'vel XCF error': dfile['x_v_e'],
                               'lambda spectral width XCF': dfile['x_w_l'],
                               'lmabda spectral width error XCF': dfile['x_w_l_e'],
                               'sigma spectral width XCF': dfile['x_w_s'],
                               'sigma spectral width error XCF': dfile['x_w_s_e'],
                               'phase at lag0': dfile['phi0'],
                               'phase at lag0 error': dfile['phi0_e'],
                               'elevation estimate': dfile['evl'],
                               'low elevation estimate': dfile['evl_low'],
                               'high elevation estimate': dfile['evl_high'],
                               'std lambda XCF': dfile['x_sd_l'],
                               'std sigma XCF': dfile['x_sd_s'],
                               'std phi XCF': dfile['x_sd_phi']}
                beamdata = beamrecord(scalardata,vectordata)
            self.datarecords.append(beamdata)





