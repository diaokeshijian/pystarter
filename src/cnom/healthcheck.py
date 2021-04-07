import paramiko

ssh_conn = paramiko.SSHClient()
serverIP = ''
serverPort = 0
username = ''
password = ''
serverProps = {}


def load_prop():
    propFile = open('Server_Prop','r')
    propFileLines = propFile.readlines()
    global serverIP
    global serverPort
    global username
    global password
    for line in propFileLines:
        if 'serverIP' in line:
            serverIP = get_prop_value(line)
        elif 'serverPort' in line:
            serverPort = get_prop_value(line)
        elif 'username' in line:
            username = get_prop_value(line)
        elif 'password' in line:
            password = get_prop_value(line)


def get_prop_value(line) -> str:
    tmp = line.split('=')[1]
    tmp = tmp.strip()
    return tmp


def connect():
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.connect(serverIP, port=serverPort, username=username, password=password)


def exe_command():
    stdin, stdout, stderr = ssh_conn.exec_command("bash -lc 'cnomctl status'")
    print(stdout.read().decode('utf-8'))


load_prop()
connect()
exe_command()
ssh_conn.close()


