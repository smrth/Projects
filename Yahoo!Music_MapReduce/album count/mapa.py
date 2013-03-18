
file1 = open('albumData1.txt')

import sys


for line in file1.readlines():
	line=line.strip()
	i=line.split('|')
	print i[1]+','+str(1)
