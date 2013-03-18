
file1 = open('/home/samarts/it1.txt')

import sys


for line in file1.readlines():
	line=line.strip()
	i=line.split('	')
	print i[0]+','+i[1]+','+str(1)
