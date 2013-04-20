#Write a program to determine the Mth to last element of a list.

import sys

def ele(line,last):
    return line[-last-1:-last]  
  

f = open(sys.argv[1],'r')
    
for i in f.readlines():
    i=i.strip()
    line=i.split(' ') 
    count = len(line)-1
    last= int(line[count])
    if (int(count) < int(last) ):
        pass
    else:
        final = ele(line,last)
        print final[0]
