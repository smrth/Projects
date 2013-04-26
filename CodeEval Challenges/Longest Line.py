#Write a program to read a multiple line text file and write the 'N' longest lines to stdout. 
#Where the file to be read is specified on the command line.

import sys

f = open(sys.argv[1],'r')

list =[]
non_blank_count = 0

for i,line in enumerate(f):
    if (i == 0):
        count = line.strip()
    else:
        line=line.strip()
        list.append(line)
        
list = sorted(list, key = len, reverse = True)
for i in range(int(count)):
    print list[i]