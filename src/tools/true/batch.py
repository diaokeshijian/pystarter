#!/usr/bin/python

##############################
# Name: Send ENMCLI command  #
##############################

import enmscripting
import sys

########
# Main #
########

if not len(sys.argv) > 1:
        print "Usage:"
        print "# python batch.py <full path to batch file>"
        sys.exit(0)
else:
        inputfile=sys.argv[1]

enm_url = 'https://enmnth.rfterranenm1.net'
enm_user = 'Administrator'
enm_pass = 'TestPassw0rd'

try:
        f = open(inputfile, 'r')
        content = f.readlines()
finally:
        f.close()

session = enmscripting.open(enm_url, enm_user, enm_pass)
terminal = session.terminal()

for cmd in content:
        result = terminal.execute(cmd)
        print(result)

enmscripting.close(session)
