import os

log_file_path = "C:\Users\ebenyue\OneDrive - Ericsson AB\Project\License_True\Lots of PO's license\checked\MTG\ENIQ1_MTG_License_Installation_Logs\\"
modified_log_path = ''
file_list = os.listdir(log_file_path)

for log_file in file_list:
    original_file_path = log_file_path + log_file
    print original_file_path
    original_file = open(original_file_path, 'r').readlines()
    modified_file_name = modified_log_path + log_file
    print modified_file_name
    modified_file = open(modified_file_name, 'a')
    for line in original_file:
        if line.startswith('rosseniqstyn1'):
            modified_file.write(line.replace('rosseniqstyn1', 'rosseniqsmtg1'))
        else:
            modified_file.write(line)
    modified_file.close()
