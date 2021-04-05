import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.169.64.212', port = 22, username= 'cnom', password='shroot12')
stdin, stdout, stderr = ssh.exec_command("bash -lc 'cnomctl status'")

#print(stdin.read().decode('utf-8'))
print(stdout.read().decode('utf-8'))

ssh.close()