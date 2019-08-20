import sys


node_id_file = open('C:\\Users\ebenyue\\Desktop\\bb_node_list.txt')
nodes_id_list = node_id_file.readlines()

print len(nodes_id_list)

for node in nodes_id_list:
    node = node.replace('\n', '')
    print node
