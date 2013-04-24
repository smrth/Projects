#You are given several strings that may/may not be valid emails. 
#You should write a regular expression that determines if the email id is a valid email id or not. 
#You may assume all characters are from the english language.

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