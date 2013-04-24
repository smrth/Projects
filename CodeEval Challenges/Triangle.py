import sys

f = open(sys.argv[1],'r')

list =[]
non_blank_count = 0

for line in f:
    if line.strip():
        line = line.strip()
        list.append(line.split(" "))
        non_blank_count += 1
count = non_blank_count-2

while(count != 0 ):
    temp = []
    for index in range(len(list[count])-1):
        index1 = list[count+1][index]
        index2 = list[count+1][index+1]
        total1= int(index1) + int(list[count][index])
        total2= int(index2) + int(list[count][index])
        great = total2 if total1 <= total2 else total1
        temp.append(great)
    list.pop(count)
    list.pop(count)
    list.append(temp)
    count = count - 1
final=int(list[0][0])+int(list[1][0])
print final
f.close()  