file=open("./a.txt","r")
ln=0
wn=0
cn=0
for line in file:
	ln+=1
	wn+=len(line.split())
	cn+=len(line)
print("number of lines ",ln)
print("number of words ",wn)
print("number of charectors ",cn)
