#!/usr/bin/python
# coding:utf-8
import os

# locate the files:
base_path = "C:\\Users\\benwe\\OneDrive - Ericsson AB\\Project\\License_True\\Lots of PO's license\\checked\\MTG\\backup\\"

# os.listdir 列出该目录中所有文件
files = os.listdir(base_path)

for file in files:
    print "the orginal file name is : " + file
    old_file = os.path.join(base_path + file)
    new_file = os.path.join(base_path + file.replace('.txt', '') + '.log')
    os.rename(old_file, new_file)




