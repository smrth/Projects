f = open("/Users/Samarth_old/Desktop/Data881/Project/mapcoount/mr.txt","w+")

from operator import itemgetter

import sys
current_song = None
current_count = 0
word = None
song = 0
i=[]
j=[]
final=[]
ff=[]
k=0

for line in sys.stdin:
	line = line.strip()
	global song
	song, count=line.split(',',1)
	try:
		count = int(count)
	except ValueError:
		continue
	if current_song == song:
		current_count += count
	else:
		if current_song:
			line1=(str(current_song),str(current_count))
                        j.append(line1)
		current_count = count
		current_song = song

global song
if current_song == song:
	line1=(str(current_song),str(current_count))
	j.append(line1)

#ff=sorted(j,key=itemgetter(1),reverse=True)

leng=len(j)
for ij in range(leng):
        tt=str(j[ij][0])+'	'+str(j[ij][1])+'\n'
        f.write(tt)
