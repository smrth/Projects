import sys
from operator import itemgetter

correct = True
word =[]
current_word = None
current_count = 0
line = 0
j=[]

while(correct):
    words=input()
    if (( int(words) >= int(1000000))):
        correct = True
    else:
        correct = False

while(line < words):
    answer=raw_input()
    word.append(int(answer))
    line = line + 1

d=sorted(word,reverse=True)

for i in range(0,4):
    print d[i]  