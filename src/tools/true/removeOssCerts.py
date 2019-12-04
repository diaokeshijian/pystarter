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
enm_user = 'leigu001_v11'
enm_pass = 'Password1234'

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
    output_lines = output.get_output()
    _enm_certs = []
    _oss_certs = []
    for line in output_lines:
        fdn = ''
        if line.startswith('FDN'):
            fdn = line.split('TrustedCertificate=')
            trustedCertificateId = fdn[1]
        if line.startswith('certificateContent'):
            if 'OU=EnmNth' in line:
                _enm_certs.append(trustedCertificateId)
            else:
                _oss_certs.append(trustedCertificateId)
    _certs = {'oss_certs': _oss_certs, 'enm_certs': _enm_certs}
    return _certs


# 2.    set managedState to disable for each of the OSS-RC certificate
def disableOssCertificates(osscerts, _node):
    for cert_id in osscerts:
        _command_disable_OssRC_Cert = 'cmedit set SubNetwork=RadioNode,MeContext=' + _node + ',ManagedElement=' + \
                                      _node + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=' + str(cert_id) + \
                                      ' managedState=DISABLED --force '
        _response = terminal.execute(_command_disable_OssRC_Cert)
        logging.info(_response)
        _response_lines = _response.get_output()
        response_line = ''
        for line in _response_lines:
            response_line = response_line + line
        if 'SUCCESS FDN' not in response_line:
            print '[FAIL] set OSS certs managedState FAILED! Node name: ' + _node + '; OSS certs id: ' + cert_id + '.'
            exit(1)


# 3.	Remove the OSS-RC CAs by setting the NE TrustCategory to contain ONLY the ENM TrustedCertificate FDNs
def setTrustedCategorywithEnmCerts(enmcerts, _node):
    command_certificates_in_TrustedCategory = 'cmedit get ' + _node + ' TrustCategory.TrustedCertificates'
    _response = terminal.execute(command_certificates_in_TrustedCategory)
    logging.info(_response)
    trustedCertificates = ''
    for _oss_cert_id in enmcerts:
        tmp = '"SubNetwork=RadioNode,MeContext=' + _node + ',ManagedElement=' + node + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=' + _oss_cert_id + '",'
        trustedCertificates = trustedCertificates + tmp
    trustedCertificates = trustedCertificates[0: -1]
    command_remove_osscerts_from_trusted_category = 'cmedit set SubNetwork=RadioNode,MeContext=' + _node + ',ManagedElement=' + _node + ',SystemFunctions=1,SecM=1,CertM=1,TrustCategory=1 trustedCertificates=[' + trustedCertificates + ']'
    print 'command_remove_osscerts_from_trusted_category : ' + command_remove_osscerts_from_trusted_category
    _response = terminal.execute(command_remove_osscerts_from_trusted_category)
    _response_code = _response.http_response_code()
    print 'stage : setTrustedCategorywithEnmCerts'
    print _response_code
    logging.info(command_remove_osscerts_from_trusted_category)
    logging.info(_response)
    _response_lines = _response.get_output()
    response_line = ''
    for line in _response_lines:
        response_line = response_line + line
        logging.info(response_line)
    if 'SUCCESS FDN' not in response_line:
        print '[FAIL] Remove Oss-RC certificates from TrustCategory FAILED! Node name: ' + _node
        exit(3)


# 4.	Remove the OSS-RC CA certs from the NE by executing the following command for each TrustedCertificate not
#       included in the TrustCategory.
def removeOssCertsFromNE(osscerts, node):
    for cert_id in osscerts:
        command_remove_oss_certs_from_ne = 'cmedit action SubNetwork=RadioNode,MeContext=' + node + ',' \
                                           'ManagedElement=' + node \
                                           + ',SystemFunctions=1,SecM=1,CertM=1 removeTrustedCert.(trustedCert=' \
                                             '"SubNetwork=RadioNode,MeContext=' + node + ',ManagedElement=' + node + \
                                           ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=' + cert_id + '")'
        logging.info('command_remove_oss_certs_from_ne: ' + command_remove_oss_certs_from_ne)
        _response = terminal.execute(command_remove_oss_certs_from_ne)
        _response_code = _response.http_response_code()
        logging.info('stage : removeOssCertsFromNE')
        logging.info(_response_code)
        logging.info(_response)
        _response_lines = _response.get_output()
        print ('len(_response_lines):')
        print len(_response_lines)
        print command_remove_oss_certs_from_ne
        response_line = ''
        for line in _response_lines:
            response_line = response_line + line
        if 'SUCCESS FDN' not in response_line:
            print '[FAIL] remove OSS-RC certificates from NE failed! Node name : ' + node + 'Certificate ID : ' + cert_id
            exit(4)


#node_file = open(sys.argv[1])
node_file = open('C:\\Users\\ebenyue\\OneDrive - Ericsson AB\\Project\\004 _ Thailand_TRUE_Migration\\Migration_Day6_One_PICO_Node\\ne_id_list.txt')
node_list_lines = node_file.readlines()
node_list = []
for line in node_list_lines:
    line = line.replace('\n', '')
    node_list.append(line)

for node in node_list:
    certs_in_node = sortCertificates(node)
    oss_certs = certs_in_node.get('oss_certs')
    enm_certs = certs_in_node.get('enm_certs')
    disableOssCertificates(oss_certs, node)
    setTrustedCategorywithEnmCerts(enm_certs, node)
    removeOssCertsFromNE(oss_certs, node)
    print 'OSS certificates removed successfully for node : ' + node

# logging.info('Program started!')
