artist_file = open("/home/aby/Desktop/881_proj/artist.txt")
f5 = open("/Users/Samarth/Desktop/artist.txt","w+")

artist_list=[]

for line in artist_file.readlines():		#to get artist
	line=line.strip()
	line=line.split('|')
	sa_list=(int(line[0]),int(line[2]))
	artist_list.append(sa_list)


for line1 in sys.stdin:
	line1=line1.strip()
	songid=line1
	for entry in artist_list:
		if(str(songid) == str(entry[0])):		#got song in file
			tt=str(entry[2])+'\n'
			f5.write(tt)
	
	
	
