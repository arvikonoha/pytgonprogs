n=int(input("enter the number of elements in the list "))
print("enter the list elements ")
li=[]
for i in range(0,n):
	li.append(int(input()))

def indexOfSmallestElement(li):
	minindex=0
	mi=li[0]
	for i in range(0,n):
		if li[i] < mi:
			mi=li[i]
			minindex=i
	return minindex
print("lowest element in the list is present at the index ",indexOfSmallestElement(li))
