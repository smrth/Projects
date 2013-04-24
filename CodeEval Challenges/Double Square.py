#A double-square number is an integer X which can be expressed as the sum of two perfect squares. For example, 10 is a double-square because 10 = 3^2 + 1^2. 

import sys
import math

total = 0
pair=[]

f = open(sys.argv[1],'r')

for i,line in enumerate(f):
    if (i == 0):
        count = line.strip()
    elif ( int(count) <= 100 and int(count) >= 1):
        line=line.strip()
        total = 0
        if ( line.strip() and int(line) <= 2147483647 and int(line)>=0):
            for j in range(int(math.sqrt(int(line)))):
                num2 = math.sqrt(int(line) - ( j * j ))
                temp=(j,num2)
                pair.append(temp)
                if ( ((num2) - int(num2)) == 0):
                    if (num2,j) in pair:
                        pass
                    else:
                        total = total +1
            print total
    else:
        pass
        break