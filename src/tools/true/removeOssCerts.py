#!/usr/bin/python

#################################################################################################
# Name: Cleanup scripts after migration
# Desription: Removal of Source ENM CA Certificates from RadioNode
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

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_dir + 'Remove_original_certificate_' + str(time.strftime('%Y%m%d%H%M%S')) + '.log',
                    filemode='a')

logging.info('Program started!')


def getEnmNodeCredId(node_name):
    _enmNodeCredentialId = 0  # type: int
    isEnmCredential = False
    command = 'cmedit get ' + node_name + ' NodeCredential.*'
    output = terminal.execute(command)
    lines = output.get_output()
    for line in lines:
        fdn = ''
        if line.startswith('FDN'):
            fdn = line.split('NodeCredential=')
            _enmNodeCredentialId = fdn[1]
        if line.startswith('certificateContent '):
            if 'http://10.81.10' in line:
                isEnmCredential = True
                break
    return _enmNodeCredentialId


logging.info('establish ENM terminal session:')
session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()
logging.info('ENM terminal session established!')

node_file = open(sys.argv[1])
node_list = node_file.readlines()

for node in node_list:
    enmNodeCredentialId = getEnmNodeCredId(node)
    print 'enm credId : ' + str(enmNodeCredentialId)
