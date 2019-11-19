import re
mystr=input("enter the string ")
piter=re.finditer(r"[A-Z]",mystr)
indices=[i.start() for i in piter]
print("number of capital letters is ",len(indices))
print("positions of capital letters ",indices)

