import re
mystr=input("enter the string ")
vowelMap={"a":0,"e":0,"i":0,"o":0,"u":0,"A":0,"E":0,"I":0,"O":0,"U":0}
for key in vowelMap:
        vowelMap[key]=len(re.findall(r""+key,mystr))
        print("number of ",key,vowelMap[key])

