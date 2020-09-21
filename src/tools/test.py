import datetime

#lte_subnetwork_file = open('C:\\Users\\ebenyue\\Downloads\\subnetworks.txt')

#for line in lte_subnetwork_file:
#    print line + '_'
#    line = line.strip()
#    print line + '_'
now = datetime.datetime.now()

date = now.strftime('%Y%m%d_%H:%M:%S')
print date
