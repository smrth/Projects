
file1 = open('/Users/Samarth/Desktop/a/trackData1.txt')

import sys


for line in file1.readlines():
	line=line.strip()
	i=line.split('|')
	print i[2]+','+str(1)
