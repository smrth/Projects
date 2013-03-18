f = open("/home/samarts/avg/avgall.txt","w+")
f2 = open("/home/samarts/avg/scoresort.txt","w+")

from operator import itemgetter

import sys
current_song = None
current_count = 0
current_score = 0
song = 0
avg= 0
word = None
i=[]
j=[]
final=[]
ff=[]
k=0

for line in sys.stdin:
	global song
	line = line.strip()
	song, score, count=line.split(',',2)
	try:
		count = int(count)
		score = int(score)
	except ValueError:
		continue
	if current_song == song:
		current_count = current_count + count
		current_score = current_score + score
	else:
		if current_song:
			avg = current_score/current_count
			line1=(int(current_song),int(current_count),int(current_score),int(avg))
                        j.append(line1)
		current_count = count
		current_song = song
		current_score = score
		avg = current_score/current_count

if current_song == song:
	avg = current_score/current_count
	line1=(int(current_song),int(current_count),int(current_score),int(avg))
	j.append(line1)

ff=sorted(j,key=itemgetter(1),reverse=True)
aa=sorted(j,key=itemgetter(2),reverse=True)

leng=len(ff)
for ij in range(leng):
        tt=str(ff[ij][0])+'	'+str(ff[ij][1])+'	'+str(ff[ij][2])+'	'+str(ff[ij][3])+'\n'
        f.write(tt)

leng1=len(aa)
for ia in range(leng1):
        tt1=str(aa[ia][0])+'     '+str(aa[ia][1])+'      '+str(aa[ia][2])+'      '+str(aa[ia][3])+'\n'
        f2.write(tt1)
