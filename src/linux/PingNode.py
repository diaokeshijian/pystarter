#!/usr/bin/env python
# coding:utf-8

import sys
import os

if len(sys.argv) != 2:
    print ""
    print "Usage: "
    print "python PingNode.py <full_path_to_node_file.txt>"
    print ""
    sys.exit(0)
else:
    print sys.argv[1]

nodeIpFile = open(sys.argv[1])
nodeIpList = []

for line in nodeIpFile:
    line = line.strip('\n')
    if len(line) > 0:
        nodeIpList.append(line)

#print len(nodeIpList)
#print nodeIpList

for ip in nodeIpList:
    backInfo = os.popen('ping -c 1 %s' % ip)
    print '***backInfo start**'
    print backInfo
    print '****backinfo end****'

#    backInfo = str(backInfo)
#    if backInfo.find('1 packets transmitted, 1 received, 0% packet loss'):
#        print ip + ' is alive'





