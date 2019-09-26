file = open('1.txt')
line_list = []
for each in file:
    each = each.replace('\n', '')
    line_list.append(each)

print len(line_list)

for line in line_list:
    print line + '1'