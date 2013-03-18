file1 = open('/scratch/samarts/fout.txt')
f1 = open("/scratch/samarts/files/file1.txt","w+")
f2 = open("/scratch/samarts/files/file2.txt","w+")
f3 = open("/scratch/samarts/files/file3.txt","w+")
f4 = open("/scratch/samarts/files/file4.txt","w+")
f5 = open("/scratch/samarts/files/file5.txt","w+")
f6 = open("/scratch/samarts/files/file6.txt","w+")
i=[]
k = 0

for line in file1.readlines():
	if ( k >= 0 and k < 42133380 ):
		i=line.strip().split('	')
		line=i[0]+"	"+i[1]+"	"+i[2]+"	"+i[3]+"	"+i[4]+"\n"
		f1.write(line)
		k = k + 1
        if ( k >= 42133380 and k < 84266760 ):
                i=line.strip().split('	')
                line=i[0]+"     "+i[1]+"        "+i[2]+"        "+i[3]+"        "+i[4]+"\n"
                f2.write(line)
		k = k + 1
        if ( k >= 84266760 and k < 126400140 ):
                i=line.strip().split('	')
                line=i[0]+"     "+i[1]+"        "+i[2]+"        "+i[3]+"        "+i[4]+"\n"
                f3.write(line)
		k = k + 1
        if ( k >= 126400140 and k < 168533520 ):
                i=line.strip().split('	')
                line=i[0]+"     "+i[1]+"        "+i[2]+"        "+i[3]+"        "+i[4]+"\n"
                f4.write(line)
		k = k + 1
        if ( k >= 168533520  and k < 210666900 ):
                i=line.strip().split('	')
                line=i[0]+"     "+i[1]+"        "+i[2]+"        "+i[3]+"        "+i[4]+"\n"
                f5.write(line)
		k = k + 1
        if ( k >= 210666900  and k < 252800276 ):
                i=line.strip().split('	')
                line=i[0]+"     "+i[1]+"        "+i[2]+"        "+i[3]+"        "+i[4]+"\n"
                f6.write(line)
		k = k + 1
