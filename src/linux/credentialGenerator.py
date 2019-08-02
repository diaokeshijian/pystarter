import sys

if len(sys.argv) < 3:
    print ""
    print "Usage: "
    print "python credentialGenerator.py <full_path_to_node_file.txt> <full_path_to_generated_credential_file>"
    print ""
    sys.exit(0)
elif len(sys.argv) > 3:
    print "Too much arguments!"
    print ""
    print "Usage: "
    print "python credentialGenerator.py <full_path_to_node_file.txt> <full_path_to_generated_credential_file>"
    print ""
    sys.exit(0)
else:
    node_list_file = sys.argv[1]
    destination_directory = sys.argv[2]

destination_directory = str(destination_directory)
if destination_directory.endswith('/') | (destination_directory.endswith('\\')):
    print destination_directory
else:
    destination_directory = destination_directory + '/'
    print destination_directory

header = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
Nodes_start = '<Nodes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
Nodes_end = "</Nodes>"
node_start = "<Node>"
node_end = "</Node>"
# for ldapCredential:
NodeFDN_start = "<NodeFdn>"
NodeFDN_end = "</NodeFdn>"
tlsMode_start = "<tlsMode>"
tlsMode_end = "</tlsMode>"
userLabel_start = "<userLabel>"
userLabel_end = "</userLabel>"
useTls_start = "<useTls>"
useTls_end = "</useTls>"
# for nodeCredential:
EntityProfileName_start = "<EntityProfileName>"
EntityProfileName_end = "</EntityProfileName>"
nodeFDN_start = "<nodeFdn>"
nodeFDN_end = "</nodeFdn>"
# common punctuations
table = '\t'
double_table = '\t\t'
enter = '\n'

nodes = []
file_node = open(node_list_file)
LdapCredential = open(destination_directory + 'LdapCredential.xml', 'w')
NodeCredential = open(destination_directory + 'NodeCredential.xml', 'w')


def ldap_credential_generation(node_list):
    LdapCredential.write(header + enter)
    LdapCredential.write(Nodes_start + enter)
    for node in node_list:
        if len(node) >0:
            LdapCredential.write(table + node_start + enter)
            LdapCredential.write(double_table + nodeFDN_start + node + nodeFDN_end + enter)
            LdapCredential.write(double_table + tlsMode_start + 'LDAPS' + tlsMode_end + enter)
            LdapCredential.write(double_table + userLabel_start + 'ENM' + userLabel_end + enter)
            LdapCredential.write(double_table + useTls_start + 'true' + useTls_end + enter)
            LdapCredential.write(table + node_end + enter)
    LdapCredential.write(Nodes_end + enter)


def node_credential_generation(node_list):
    NodeCredential.write(header + enter)
    NodeCredential.write(Nodes_start + enter)
    for node in node_list:
        print len(node)
        if len(node) > 0:
            print("write!!")
            NodeCredential.write(table + node_start + enter)
            NodeCredential.write(double_table + NodeFDN_start + node + NodeFDN_end + enter)
            NodeCredential.write(double_table + EntityProfileName_start + 'DUSGen2OAM_CHAIN_EP' + EntityProfileName_end +
                                 enter)
            NodeCredential.write(table + node_end + enter)
    NodeCredential.write(Nodes_end + enter)


try:
    for line in file_node:
        line = line.replace('\n', '')
        nodes.append(line)
finally:
    file_node.close()

try:
    ldap_credential_generation(nodes)
    node_credential_generation(nodes)
finally:
    LdapCredential.close()
    NodeCredential.close()
