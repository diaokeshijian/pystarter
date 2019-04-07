class node(object):
    node_name = ''
    node_credentials = []
    

log_file = open("C:\\Users\\ebenyue\\OneDrive - Ericsson AB\\Project\\002 _ Thailand_TRUE_OSS&ENM Migration\\1.txt")

command_printout = log_file.read()

lines = command_printout.split('\n')

mecontext = ''
nodes_all = {}

def is_there_any_uncertificated_node(node_list):
    uncertificated_nodes = []
    for node in node_list:
        if node_list.get(node).node_credentials == 'oss':
            uncertificated_nodes.append(node)
    return uncertificated_nodes

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

uncertificated_nodes = is_there_any_uncertificated_node(nodes_all)
if uncertificated_nodes:
    print 'below nodes have not been certificated by ENM:'
    print '*************************************' 
    for node in uncertificated_nodes:
        print node
    print '*************************************' 
else:
    print "all nodes certificated by ENM!"