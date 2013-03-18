from operator import itemgetter

file1 = open('/home/samarts/part-00000')
f = open("/home/samarts/rating.txt","w+")
i=[]
j=[]
final=[]
ff=[]
k=0

for line in file1.readlines():
        i=line.strip().split('	')
	temp=(int(i[0]),int(i[1]))
	j.append(temp)
ff=sorted(j,key=itemgetter(1),reverse=True)
leng=len(ff)

leng=len(ff)

for ij in range(leng):
	line=str(ff[ij][0])+'	'+str(ff[ij][1])+'\n'
	if (ff[ij][1]>100000):
		line=str(ff[ij][0])+'   '+str(ff[ij][1])+'	high\n'
		f.write(line)
for ij in range(leng):
        line=str(ff[ij][0])+'   '+str(ff[ij][1])+'\n'
        if (ff[ij][1]>100000):
                line=str(ff[ij][0])+'   '+str(ff[ij][1])+'	medium\n'
                f.write(line)
for ij in range(leng):
        line=str(ff[ij][0])+'   '+str(ff[ij][1])+'\n'
        if (ff[ij][1]>100000):
                line=str(ff[ij][0])+'   '+str(ff[ij][1])+'	low\n'
                f.write(line)

