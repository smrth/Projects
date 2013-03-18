file1 = open("/home/samarts/fout.txt")
f = open("/home/samarts/avg/favg.txt","w+")

uscore=0
count=0

for line in file1.readlines():
    i=line.strip().split('\t')
    score=i[2]
    uscore = str(int(score) + int(uscore))
    count = str(int(count) + 1)
    avg = str(int(uscore) / int(count))

f.write(uscore)
f.write("\n")
f.write(count)
f.write("\n")
f.write(avg)
f.write("\n") 
