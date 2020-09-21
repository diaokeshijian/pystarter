#!/usr/bin/python
import sys

import enmscripting
import logging
import time
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')

log_dir = './'

enm_url = 'https://enmnth.rfterranenm1.net'
enm_user = 'exportltecm'
enm_pass = 'Yffs#60!'

#################
# Logging
#################

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_dir + 'Delete_Unsync_NE_In_ENM_' + str(time.strftime('%Y%m%d%H%M%S')) + '.log',
                    filemode='a')

logging.info('Program started!')

logging.info('establish ENM terminal session:')
session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()
logging.info('ENM terminal session established!')

#ne_file = open(sys.argv[1])
ne_file = open('C:\\Users\\ebenyue\\Desktop\\ne_list.txt')
ne_list = []

for line in ne_file:
    line = line.replace('\\n', '')
    ne_list.append(line)

for ne in ne_list:
    command_get_sync_status = 'cmedit get ' + ne + ' --detailnode'
    output = terminal.execute(command_get_sync_status)
    output_lines = output.get_output()
    # output_in_one_line = ''
    # for line in output_lines:
    #     output_in_one_line = output_in_one_line + line
    # print 'output in one line : ' + output_in_one_line
    # if 'UNSYNCHRONIZED' not in output_in_one_line:
    #     print 'can not delete ' + ne + '!'
    # else:
    #     print 'will delete ' + ne + '!'
    if 'syncStatus : UNSYNCHRONIZED' not in output_lines:
        print 'can\'t delete ' + ne + '!'
    else:
        command_delete_ne = 'cmedit delete NetworkElement=' + ne + '  -ALL --force'
        delete_out_put = terminal.execute(command_delete_ne)
        print delete_out_put
        logging.info(delete_out_put)


