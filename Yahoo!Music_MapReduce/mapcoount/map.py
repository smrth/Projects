
file1 = open('/Users/Samarth_old/Desktop/Data881/Project/mapcoount/m.txt')

import sys


for line in file1.readlines():
	i=line.split('|')
	print i[1]+','+str(1)
