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

log_dir = './'

enm_url = 'https://enmnth.rfterranenm1.net'
enm_user = 'Administrator'
enm_pass = 'TestPassw0rd'

#################
# Logging
#################

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_dir + 'Remove_original_certificate_' + str(time.strftime('%Y%m%d%H%M%S')) + '.log',
                    filemode='a')

logging.info('Program started!')

logging.info('establish ENM terminal session:')
session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()
logging.info('ENM terminal session established!')


#################
# Main
#################

# 1.	Distinguish the FDNs of the TrustedCertificates that are issued by ENM and OSS-RC by executing the following
#       command and checking the issuer CN:
def sortCertificates(_node):
    command_get_all_certificates = 'cmedit get ' + _node + ' TrustedCertificate.*'
    output = terminal.execute(command_get_all_certificates)
    logging.info(output)
    response_code = output.http_response_code()
    print 'response code : ' + str(response_code)

    print type(output)
    output_lines = output.get_output()
    print type(output_lines)

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


certs = sortCertificates('CMI2021T_2NB01')
osscerts = certs.get('oss_certs')
enmcerts = certs.get('enm_certs')

print 'oss certs: '
for cert_id in osscerts:
    print cert_id
    logging.info(cert_id)
print 'enm certs: '
for cert_id in enmcerts:
    print cert_id
    logging.info(cert_id)
