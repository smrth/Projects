import sys
from operator import itemgetter

correct = True
word =[]
line = 0
output=[]

while(correct):
    words=input()
    if (( int(words) <= int(2)) or ( int(words) >= int(1000))):
        correct = True
    else:
        correct = False

while(line < words):
    answer=raw_input()
    word.append(int(answer))
    line = line + 1
        
for i in range(len(word)):
    result=1
    for j in range(len(word)):
        if (int(i) == int(j)):
            pass
        else:
            result= (int(result) * int(word[j]))
    output.append(int(result))

for i in range(len(output)):
    print output[i]