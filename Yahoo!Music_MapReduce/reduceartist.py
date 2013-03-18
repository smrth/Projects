
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

for ij in 100:
        print ff[ij][0]