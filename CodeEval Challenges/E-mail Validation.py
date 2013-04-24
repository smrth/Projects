import sys
import re

f = open(sys.argv[1],'r')

str='^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
for i in f.readlines():
    sp=i.isspace()
    if(i != '\n' and i != '\t' and i != '\r' and sp != True):
        match = re.search(str,i)
        if match:
            print 'true'
        else:
            print 'false'
    else:
        pass
        
f.close()  