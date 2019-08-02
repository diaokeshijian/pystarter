#!/usr/bin/python

import xml.etree.ElementTree as ElementTree
import argparse
import copy

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('arne_xml', help='Exported ARNE XML from OSS-RC')
arg_parser.add_argument('out_xml', help='Filename for output XML')

args = arg_parser.parse_args()

print("Parsing XML file...")
tree = ElementTree.parse(args.arne_xml)

me_list = tree.findall('.//ManagedElement')
print("Total number of ManagedElement: %d" % len(me_list))

print("Checking for Tss entries")
for me in me_list:
    tss = me.find('Tss')
    me_id = me.find('ManagedElementId').get('string')
    entries = tss.findall('Entry')
    has_secure_entry = False
    normal_entry = None
    for entry in entries:
        type_string = entry.find('Type').get('string')
        if type_string == 'NORMAL':
            normal_entry = entry
        elif type_string == 'SECURE':
            has_secure_entry = True
            break

    if not has_secure_entry:
        print("Add SECURE entry for %s" % me_id)
        if normal_entry is None:
            print("ERROR: ManagedElement doesn't have Tss entry for NORMAL user")
            continue
        new_entry = copy.deepcopy(normal_entry)
        new_entry.find('Type').set('string', 'SECURE')
        tss.append(new_entry)

# The below code is only
# tss_el = tree.findall('./Create/SubNetwork/ManagedElement[@sourceType="CELLO"]/Tss')
# for child in tss_el:
#     if child.find('./Entry/Type[@string="SECURE"]') is None:
#         entry_el = child.find('Entry')
#         et = copy.deepcopy(entry_el)
#         t = et.find('Type')
#         t.attrib['string'] = 'SECURE'
#         child.append(et)

print("Save new XML to %s" % args.out_xml)
tree.write(args.out_xml)

print("Done")
exit(0)
