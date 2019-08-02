#!/usr/bin/env python
# coding:utf-8

import os
import time
import paramiko


class User(object):
    def __init__(self, username, password):
        self.name = username
        self.password = password


def get_connection(self, ipaddress, username, password):
    try:
        client=paramiko.SSHClient()
    except Exception,e:
        print e













os.system('ls')
time.sleep(1)
os.system('mkdir tt')
time.sleep(1)
os.system('ls')
os.system('rmdir tt')

tmp = os.popen('ls /').readlines()
print(tmp)
