import re
fstr=input("enter the first string ")
sstr=input("enter the second string ")
fstr+=sstr
fstr=re.sub(r"[^A-Z]","",fstr)
print("required string ",fstr)

