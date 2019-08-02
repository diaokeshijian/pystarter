# -*- coding: utf-8 -*-
def getNeList():
    master_service_log = open('C:\\temp\\trueThailand_bak\\masterService\\OSS1_masterservice_02-08_15.log')
    i = 0
    nodes = []
    line = master_service_log.readline()
    while line:
        if line.find('MeContext') != -1:
            line_elements = line.split('=')
            nodes.append(line_elements[-1].replace('\n', ''))
        line = master_service_log.readline()

    master_service_log.close()
    for node in nodes:
        print(node)

    nodenumber = len(nodes)
    print('Node数量为: ' + str(nodenumber))


getNeList()
