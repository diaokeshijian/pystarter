#!/usr/bin/env python
# coding:utf-8

import os
import time
import paramiko


ipaddr = "192.168.47.128"
port = 22
username = "ecap"
password = "ecap123"
sshClient = paramiko.SSHClient()
sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    sshClient.connect(ipaddr, port, username, password, timeout=10)
    cmd = "mkdir /home/ecap/test11"
    cmd1 = "ls /home/ecap"
    stdin, stout, stderr = sshClient.exec_command(cmd1)
    print stout.read()
finally:
    sshClient.close()

