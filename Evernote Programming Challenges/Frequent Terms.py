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
    if (( int(words) >= int(300000)) or (int(words) <= int(0))):
        correct = True
    else:
        correct = False

while(line < words):
    answer=raw_input(),'1'
    if ((len(answer[0])>= int(25)) or (len(answer[0]) <= int(0))):
        1
    else:
        word.append(answer)
        line = line + 1
        
total=input()
word.sort()  

for l in word:
    word = l[0]
    count=l[1]
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            line1=(str(current_word),str(current_count))
            j.append(line1)
        current_count = count
        current_word = word

if current_word == word:
    line1=(str(current_word),str(current_count))
    j.append(line1)

j=sorted(j,key=itemgetter(1),reverse=True)
for k in range(total):
    print j[k][0]
