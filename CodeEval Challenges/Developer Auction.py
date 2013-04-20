#Choose a number, reverse its digits and add it to the original. If the sum is not a palindrome, repeat this procedure.

import sys

count = 0
is_p = True 
def is_pal(s):
    return s == s[::-1] 
 
def rev(x):
        result=0
        i=0
        while x/10 > 0:
                result = (result * 10) + (x % 10)
                x = x/10
        result = (result * 10) + (x % 10)
        return result  


f = open(sys.argv[1],'r')

for i in f.readlines():
    i=i.strip()
    is_p = True
    count = 0
    while(is_p and int(count)<1000 and int(i) < 4294967295):
        reverse=rev(int(i))
        pal=int(reverse)+int(i)
        p=str(pal)
        is_check=is_pal(p)
        if (is_check == True ):
            is_p = False
        i = pal
        count=count + 1
    print str(count)+" "+str(pal)
        
f.close()  