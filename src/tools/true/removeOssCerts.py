#!/usr/bin/python

#################################################################################################
### Name: Cleanup scripts after migration
### Desription: Removal of Source ENM CA Certificates from RadioNode
#################################################################################################

import logging
import os
import sys
import time
import datetime

ts = time.time()  # type: float
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')
cli_app = '/opt/ericsson/enmutils/bin/cli_app "'
cli_app_end = '"'
node_id_file = open(sys.argv[1])
#node_id_file = open('C:\\Users\\ebenyue\\Desktop\\bb_node_list')
nodes_id_list = node_id_file.readlines()
certs_Nunber = 0
for node in nodes_id_list:
    node = node.replace('\n', '')
    command_get_node_certs = cli_app + 'cmedit get ' + node + ' TrustedCertificate.certificateContent' + cli_app_end
    print command_get_node_certs
    node_certs_printout = os.popen(command_get_node_certs).readlines()
    for line in node_certs_printout:
        line = line.replace('\n', '')
        if line.startswith('FDN'):
            FDN = line.split('TrustedCertificate=')
            certs_Nunber = FDN[1]
            print certs_Nunber
        if line.startswith('certificateContent'):
            if 'issuer=CN=ENM' not in line:
                command_remove_oss_certs = cli_app + 'cmedit remove ' + node + ' certsNo: ' + certs_Nunber + cli_app_end
                print command_remove_oss_certs

