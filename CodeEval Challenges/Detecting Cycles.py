#Given a sequence, write a program to detect cycles within it.

import sys
import re


regex = re.compile(r'(.+ .+)( \1)+')

f = open(sys.argv[1],'r')

for line in f.readlines():
    if line.strip():
        
        match = regex.search(line)
        if match is not None:
            print match.group(1)
        else:
            pass