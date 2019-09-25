import os


def pingLinux(node_ip):
    result = os.popen('ping -c 1 ' + node_ip)
    print 'result : ' + str(result)
    result_lines = result.readlines()
    flag = False
    for line in result_lines:
        if '0% loss' in line:
            flag = True
    if flag:
        print node_ip + ' : is alive!'
    else:
        print node_ip + ' : is dead!!'


def checkcontain():
    str = '1 packets transmitted, 0 received, 100% packet loss, time 10000ms'
    str1 = '0% packet loss'
    if str1 in str:
        print 'contain'

#pingLinux('220.181.38.148')
checkcontain()
