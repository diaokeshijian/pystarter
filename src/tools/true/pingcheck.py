#!/usr/bin/python

import os
import sys


def pingSunOS(node_ip):
    result = os.popen('ping ' + node_ip)
    result_line = result.read()
    if 'alive' in result_line:
        print node_ip + ' : is alive!'
    else:
        print node_ip + ' : is dead!!'


def pingLinux(node_ip):
    result = os.popen('ping -c 1 ' + node_ip)
    result_lines = result.readlines()
    flag = False
    for line in result_lines:
        if ', 0% packet loss' in line:
            flag = True

    if flag:
        print node_ip + ' : is alive!'
    if not flag:
        print node_ip + ' : is dead!!'


node_file = open(sys.argv[1])
node_list = node_file.readlines()

isLinux = False
uname_result = os.popen('uname').read()
if 'SunOS' in uname_result:
    isLinux = False
elif 'Linux' in uname_result:
    isLinux = True
else:
    print 'Environment verification failed, script will exit.'
    sys.exit(0)

for node in node_list:
    node = node.replace('\n', '')
    if len(node) != 0:
        if not isLinux:
            pingSunOS(node)
        if isLinux:
            pingLinux(node)
