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
                    filename=log_dir + 'Delete_OSS_NodeCredential_' + str(time.strftime('%Y%m%d%H%M%S')) + '.log',
                    filemode='a')

logging.info('Program started!')

logging.info('establish ENM terminal session:')
session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()
logging.info('ENM terminal session established!')


#################
# FUNCTIONS
#################


# get current NodeCredentialId
def getEnmNodeCredId(node_name):
    _NodeCredentialId = 0  # type: int
    _ossNodeCredentialId = 0
    _enmNodeCredentialId = 0
    isEnmCredential = False
    command = 'cmedit get ' + node_name + ' NodeCredential.*'
    output = terminal.execute(command)
    lines = output.get_output()
    for line in lines:
        fdn = ''
        if line.startswith('FDN'):
            fdn = line.split('NodeCredential=')
            _NodeCredentialId = fdn[1]
        if line.startswith('certificateContent '):
            if 'C=TH,O=TrueCorp,OU=EnmNth' in line:
                credited = True  # type: bool
                _enmNodeCredentialId = _NodeCredentialId
            else:
                _ossNodeCredentialId = _NodeCredentialId
    _credentials = {'enmNodeCredentialId': _enmNodeCredentialId, 'ossNodeCredentialId': _ossNodeCredentialId}
    if credited:
        return _credentials
    else:
        return 0


#################
# MAIN
#################

node_list = []
node_file = open(sys.argv[1])
for node in node_file:
    node = node.replace('\n', '')
    node_list.append(node)

for node in node_list:
    credentials = getEnmNodeCredId(node)

    if credentials == 0:
        logging.info('node has not been certificated by ENM, node name: ' + node)
    else:
        print node
        ossNodeCredentialId = credentials['ossNodeCredentialId']
        command_change_node_https_credential = 'cmedit delete SubNetwork=RadioNode,MeContext=' + node + ',ManagedElement=' + node + ',SystemFunctions=1,SecM=1,CertM=1,NodeCredential=' + str(ossNodeCredentialId) + ' --force --ALL'
        logging.info('command_change_node_https_credential : ' + command_change_node_https_credential)
        result = terminal.execute(command_change_node_https_credential)
        logging.info(result.get_output())
        output_line = ''
        for line in result.get_output():
            output_line = output_line + line + ' ; '
        if 'SUCCESS FDN' in output_line:
            print 'SUCCEEDED to delete OSS NodeCredential for node : ' + node
        else:
            print 'FAILED to delete OSS NodeCredential for node : ' + node




