#Print out the prime numbers less than a given number N.

import sys

list=[]

f = open(sys.argv[1],'r')

for line in f.readlines():
    line=line.strip()
    list=[]
    for i in range(2,int(line)+1):
        flag = 0
        for j in range(2,(i/2)+1):
            if ( (i % j) == 0):
                flag = 1
                break
        if ( flag == 0 ):
            list.append(i)
    for m in range(len(list)-1):
        sys.stdout.write(str(list[m])+",")
    sys.stdout.write(str(list[len(list)-1]))
    print
                
        
        
f.close()