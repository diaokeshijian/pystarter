#!/usr/bin/python
import sys

import enmscripting
import logging
import time
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')

log_dir = './'

enm_url = 'https://enm.hljlt.5genm.cn/'
enm_user = 'exportltecm'
enm_pass = 'Yffs#60!'

#################
# Logging
#################

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_dir + 'Export_LTE_CM' + str(time.strftime('%Y%m%d%H%M%S')) + '.log',
                    filemode='a')

logging.info('Program started!')

logging.info('establish ENM terminal session:')
session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()
logging.info('ENM terminal session established!')

# lte subnetwork_file = open(sys.argv[1])
lte_subnetwork_file = open('C:\\Users\\ebenyue\\Downloads\\subnetworks.txt')
subnetwork_list = []

for line in lte_subnetwork_file:
    line = line.strip()
    subnetwork_list.append(line)

for subnetwork in subnetwork_list:
    timestamp = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
#   timestamp = str(datetime.datetime.now().strftime('%Y%m%d'))
    command_export_lte_cm = 'cmedit export ' \
                            '--ne SubNetwork=' + subnetwork + \
                            ' --filetype 3GPP --prettyformat true --enumtranslate false ' \
                            '--filecompression none -jn export_3GPP_' + subnetwork + '_' + 'test' + timestamp
    print command_export_lte_cm
#    output = terminal.execute(command_export_lte_cm)
#    output_lines = output.get_output()
#    logging.info(output_lines)
#    time.sleep(30)
