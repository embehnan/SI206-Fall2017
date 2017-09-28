import os
import filecmp
import re

myfile=open('mbox-short.txt','r')


for line in myfile.readlines():
    if re.search('From',line):
        print (line)
        numbers=re.findall('[0-9]+', line)
        print (numbers)
        name=re.findall('(\S*)@',line)
        print (name)
