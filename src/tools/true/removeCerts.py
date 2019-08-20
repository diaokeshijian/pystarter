#!/usr/bin/python

#################################################################################################
### Name: Cleanup scripts after migration
### Desription: Removal of Source ENM CA Certificates from RadioNode
##################################################################################################

import enmscripting
import logging
import time
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')

#################
### Variables
#################

log_dir = '/var/tmp/data_migration/LOGS/'
file_dir = '/var/tmp/data_migration/Day_10/'

enm_url = 'https://tddenm2.tac.co.th'
enm_user = 'Administrator'
enm_pass = 'TestPassw0rd'

#################
### Logging
#################

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_dir + 'Remove_original_certificate_' + str(time.strftime('%Y%m%d%H%M%S')) + '.log',
                    filemode='a')

#################
### Main
#################

logging.info('Program started!')

session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()

nodeFile = open(file_dir + 'nodes_file')
nodeName = nodeFile.readlines()

for i in range(len(nodeName)):
    nodeNameR = str(nodeName[i]).replace('\r', '').replace('\n', '')
    logging.info('--------------------------------')
    logging.info('Start removing certificate for ' + nodeNameR)
    command1 = 'cmedit get ' + nodeNameR + ' TrustedCertificate.certificateContent'
    result1 = terminal.execute(command1)
    for line in result1.get_output():
        print(line)
    command2 = 'cmedit set SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustCategory=1 trustedCertificates=[\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=5\",\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=6\",\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=7\",\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=8\"]'
    terminal.execute(command2)
    command3 = 'cmedit action SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1 removeTrustedCert.(trustedCert=\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=1\")'
    terminal.execute(command3)
    command4 = 'cmedit action SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1 removeTrustedCert.(trustedCert=\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=2\")'
    terminal.execute(command4)
    command5 = 'cmedit action SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1 removeTrustedCert.(trustedCert=\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=3\")'
    terminal.execute(command5)
    command6 = 'cmedit action SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1 removeTrustedCert.(trustedCert=\"SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,TrustedCertificate=4\")'
    terminal.execute(command6)
    logging.info('Removal of TrustCertificates for node ' + nodeNameR + ' done!')
    command7 = 'cmedit get ' + nodeNameR + ' NodeCredential.subjectName'
    result2 = terminal.execute(command7)
    for line2 in result2.get_output():
        print(line2)
    command8 = 'cmedit delete SubNetwork=ONRM_ROOT_MO,SubNetwork=RadioNodeTDD,MeContext=' + nodeNameR + ',ManagedElement=' + nodeNameR + ',SystemFunctions=1,SecM=1,CertM=1,NodeCredential=1 --force --ALL'
    terminal.execute(command8)
    logging.info('Removal of NodeCredential for node ' + nodeNameR + ' done!')
    logging.info('Finish certificate cleanup for node ' + nodeNameR)
    logging.info('--------------------------------')
enmscripting.close(session)
logging.info('Program finished!')
