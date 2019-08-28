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

# 1.	Distinguish the FDNs of the TrustedCertificates that are issued by ENM and OSS-RC by executing the following
#       command and checking the issuer CN:
def sortCertificates(_node):
    command_get_all_certificates = 'cmedit get ' + _node + ' TrustedCertificate.*'
    output = terminal.execute(command_get_all_certificates)
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


# 2.    set managedState to disable for each of the OSS-RC certificate
def disableOssCertificates(osscerts, _node):
    for cert_id in osscerts:
        _command_disable_OssRC_Cert = 'cmedit set SubNetwork=RadioNode,MeContext=' + _node + ',ManagedElement=' + _node +\
                                      ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=' + str(cert_id) + \
                                     ' managedState=DISABLED --force '
        _response = terminal.execute(_command_disable_OssRC_Cert)
        logging.info(_response)
        _response_lines = _response.get_output()
        _response_line = ''
        for line in _response_line:
            _response_line = _response_line + line
        if '1 instance(s) updated' not in _response_line:
            print '[FAIL] set managedState of OSS certs FAILED! Node name: ' + _node + '; OSS certs id: ' + cert_id + '.'


# 3.	Remove the OSS-RC CAs by setting the NE TrustCategory to contain ONLY the ENM TrustedCertificate FDNs
def setTrustedCategorywithEnmCerts(enmcerts, _node):
    command_certificates_in_TrustedCategory = 'cmedit get ' + _node + ' TrustCategory.TrustedCertificates'
    _response = terminal.execute(command_certificates_in_TrustedCategory)
    logging.info(_response)
    trustedCertificates = ''
    for _oss_cert_id in enmcerts:
        tmp = '"SubNetwork=RadioNode,MeContext=' + _node + ',ManagedElement=NKW3048X_2NB01,SystemFunctions=1,SecM=1,' \
                                                          'CertM=1,TrustedCertificate=' + _oss_cert_id + '",'
        trustedCertificates = trustedCertificates + tmp
    trustedCertificates = trustedCertificates[0: -1]
    command_remove_osscerts_from_trustedcatagory = 'cmedit set SubNetwork=RadioNode,MeContext=' + _node + ' ,' \
                                                   'ManagedElement=' + _node + ',SystemFunctions=1,SecM=1,CertM=1,' \
                                                   'TrustCategory=1 trustedCertificates=[' + trustedCertificates + ']'
    _response = terminal.execute(command_remove_osscerts_from_trustedcatagory)
    logging.info(_response)
    _response_lines = _response.get_output()
    _response_line = ''
    for line in _response_line:
        _response_line = _response_line + line
    if 'SUCCESS FDN' not in _response_line:
        print '[FAIL] Remove Oss-RC certificates from TrustCategory FAILED! Node name: ' + _node


# 4.	Remove the OSS-RC CA certs from the NE by executing the following command for each TrustedCertificate not
#       included in the TrustCategory.
def removeOssCertsFromNE(osscerts, node):
    for cert_id in osscerts:
        command_remove_oss_certs_from_ne = 'cmedit action SubNetwork=RadioNode,MeContext=NKW3048X_2NB01,' \
                                           'ManagedElement=' + node\
                                           + ' ,SystemFunctions=1,SecM =1,CertM=1 removeTrustedCert.(trustedCert=' \
                                             '"SubNetwork=RadioNode,MeContext=' + node + ',ManagedElement=' + node + \
                                           ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=' + cert_id + '")'
        _response = terminal.execute(command_remove_oss_certs_from_ne)
        logging.info(_response)
        _response_lines = _response.get_output()
        _response_line = ''
        for line in _response_lines:
            _response_line = _response_lines + line
        if 'SUCCESS FDN' not in _response_line:
            print '[FAIL] remove OSS-RC certificates from NE failed! Node name : ' + node + 'Certificate ID : ' + cert_id


node_file = open(sys.argv[1])
node_list = node_file.readlines()

for node in node_list:
    certs_in_node = sortCertificates(node)
    oss_certs = certs_in_node.get('oss_certs')
    enm_certs = certs_in_node.get('enm_certs')
    disableOssCertificates(oss_certs, node)
    setTrustedCategorywithEnmCerts(enm_certs, node)
    removeOssCertsFromNE(oss_certs, node)

# logging.info('Program started!')