import re
mystr=input("enter the string ")
filstr=""
for c in mystr:
	if c not in "'!()-[]{};:\",\,<>,/,?,@,#,$,%^&*_~":
		filstr+=c
print("filtered string ",filstr) 
