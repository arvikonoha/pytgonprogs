from functools import reduce
file=open("./marks.txt")
for line in file:
	print("student name ",line.split()[0])
	marks=line.split()[1:]
	total=reduce(lambda a,b: int(a)+int(b),marks)
	print("total marks ",total," average ",total/6)

