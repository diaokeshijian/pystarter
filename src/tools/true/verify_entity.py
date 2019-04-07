#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import time

if len(sys.argv) < 2:
    print ""
    print "Usage: "
    print "python verify_entity.py <full_path_to_node_file.txt>"
    print ""
    sys.exit(0)
elif len(sys.argv) > 2:
    print "Too much arguments!"
    print ""
    print "Usage: "
    print "python verify_entity.py <full_path_to_node_file.txt>"
    print ""
    sys.exit(0)
else:
    node_list_file = sys.argv[1]
    
    
# 
class node(object):
    node_name = ''
    node_credentials = ''



    

# ENM credentials:
username = 'leiguect'
password = 'Leiguect1234'
base_counter = 300
base_step = 300
command_printout = ''
node_list_size = 0
nodes = []
entities = []
certificated_nodes = []
not_certificated_nodes = []

# get node list:
node_file = open(node_list_file)
# get nodes:
for line in node_file:
    line = line.replace('\n', '')
    nodes.append(line)
    node_list_size = len(nodes)
print "there are ", node_list_size, "nodes to be verified!"


def transform_command_list_to_string(printout_list):
    printed_lines = ''
    for next_line in printout_list:
        # line1 = line1.replace('\n', '')
        printed_lines = printed_lines + next_line
    return printed_lines


def execute_command(nodes_list):
    nodes_in_command = ''
    for node in nodes_list:
        if node:
            node = node.replace('\n', '')
            nodes_in_command = nodes_in_command + node + ';'
    nodes_in_command = nodes_in_command[: -1]
    command = '/opt/ericsson/enmutils/bin/cli_app "cmedit get ' + nodes_in_command + ' NodeCredential.*"'
    print command
    printed_lines_list = os.popen(command).readlines()  # type: List[unicode]
    print 'command executed!'
    tmp = transform_command_list_to_string(printed_lines_list)
    print 'command printout processed!'
    return tmp


def get_certificated_node_and_not_certificated_node(prints):
    print prints
    if len(prints) == 1:
        element_tmp = prints[0].split('-')[0]
        print element_tmp
        not_certificated_nodes.append(element_tmp)
    elif len(prints) > 1:
        element_tmp = prints[0].split('-')[0]
        print element_tmp
        certificated_nodes.append(element_tmp)


def is_there_any_uncertificated_node(node_list):
    uncertificated_nodes = []
    for node in node_list:
        if node_list.get(node).node_credentials == 'oss':
            uncertificated_nodes.append(node)
    return uncertificated_nodes

# start looping:
if node_list_size <= base_counter:
    command_printout = execute_command(nodes)
elif node_list_size > base_counter:
    while node_list_size > base_counter:
        tmp_node_list = nodes[base_counter - base_step: base_counter]
        command_printout = command_printout + execute_command(tmp_node_list)
        base_counter = base_counter + base_step
    index_of_remaining_node = base_counter - base_step
    remaining_nodes = nodes[index_of_remaining_node:]
    command_printout = command_printout + execute_command(remaining_nodes)

print '*************************************'
# print command_printout
# print '*************************************'

lines = command_printout.split('\n')

mecontext = ''
nodes_all = {}

for line in lines:
    if line:
        if line.startswith('FDN'):
            fdn_in_list = line.split(',')
            mecontext = fdn_in_list[1].split('=')[1]
            # print mecontext
        if line.startswith('certificateContent'):
            if '10.81.10' in line:
                node_with_enm_cert = node()
                node_with_enm_cert.node_name = mecontext
                node_with_enm_cert.node_credentials ='enm'
                nodes_all[mecontext] = node_with_enm_cert
                # print node_with_enm_cert.node_name, node_with_enm_cert.node_credentials
            else:
                node_with_oss_cert = node()
                node_with_oss_cert.node_name = mecontext
                node_with_oss_cert.node_credentials = 'oss'
                if not nodes_all.get(node_with_oss_cert.node_name):
                    nodes_all[node_with_oss_cert.node_name] = node_with_oss_cert
                # print node_with_oss_cert.node_name, node_with_oss_cert.node_credentials
print '-------------------------------------' 
print '|  node name:    | certificated by: |'
for node in nodes_all:
    print '|', nodes_all[node].node_name, '|      ', nodes_all[node].node_credentials, '       |'      
    
print '-------------------------------------' 

for node in nodes_all:
    if nodes_all.get(node).node_credentials == 'oss':
        print nodes_all.get(node).node_name       
    
print '*************************************'    
uncertificated_nodes = is_there_any_uncertificated_node(nodes_all)
if uncertificated_nodes:
    print 'below nodes have not been certificated by ENM:'
    print '*************************************' 
    for node in uncertificated_nodes:
        print node
    print '*************************************' 
else:
    print "all nodes certificated by ENM!"

'''
printouts = command_printout.split('\n')
for printout in printouts:
    if printout.startswith('subjectName'):
        entities.append(printout)

for entity in entities:
    # print entity
    entity = entity[17:]  # UTT8505T_2NB01-oam,C=TH,O=TrueCorp,OU=EnmNth
    # print entity
    entity_elements = entity.split(',')
    get_certificated_node_and_not_certificated_node(entity_elements)

# some node may have several credentials, the node with oss credential with be put into not_certificated_node, those
# node needs to be removed from not_certificated_nodes
for node in not_certificated_nodes:
    if node in certificated_nodes:
        while node in not_certificated_nodes:
            node_index = not_certificated_nodes.index(node)
            not_certificated_nodes.pop(node_index)

time.sleep(2)
print '****************************'
print 'certificated nodes: '
for element in certificated_nodes:
    print element
print '****************************'
time.sleep(1)
print 'amount: '
print len(certificated_nodes)
print '****************************'
time.sleep(1)
print 'not certificated nodes:'
for element in not_certificated_nodes:
    print element
print '****************************'
time.sleep(1)
print 'amount: '
print len(not_certificated_nodes)
print '****************************'
'''



