#!/usr/bin/python

#################################################################################################
# Name: update Https and CliTLs scripts after migration
##################################################################################################
import sys

import enmscripting
import logging
import time
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')

#################
# Variables
#################

log_dir = './LOGS/'
file_dir = '/var/tmp/data_migration/Day_10/'

enm_url = 'https://enmnth.rfterranenm1.net'
enm_user = 'Administrator'
enm_pass = 'TestPassw0rd'

#################
# Logging
#################

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename=log_dir + 'Remove_original_certificate_' + str(time.strftime('%Y%m%d%H%M%S')) + '.log',
#                     filemode='a')
#
# logging.info('Program started!')
#
# logging.info('establish ENM terminal session:')
session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()
# logging.info('ENM terminal session established!')


#################
# Main
#################

# get all certificates on Node :
def sortCertificates(node):
    command_get_all_certificates = 'cmedit get ' + node + ' TrustedCertificate.*'
    output = terminal.execute(command_get_all_certificates)
    output_lines = output.get_output()
    enm_certs = []
    oss_certs = []
    for line in output_lines:
        fdn = ''
        if line.startswith('FDN'):
            fdn = line.split('TrustedCertificate=')
            trustedCertificateId = fdn[1]
        if line.startswith('certificateContent'):
            if 'issuer=CN=' in line:
                enm_certs.append(trustedCertificateId)
            else:
                oss_certs.append(trustedCertificateId)
    _certs = {'oss_certs': oss_certs, 'enm_certs': enm_certs}
    return _certs


certs = sortCertificates('AYT1301X_2NB03')
oss_certs = certs.get('oss_certs')
enm_certs = certs.get('enm_certs')







