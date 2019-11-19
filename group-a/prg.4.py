from functools import reduce
n=int(input("enter the number of student "))
print("enter student details ")
sarr=[ [input("student name "),float(input("student marks "))] for i in range(0,n)]
sarr=sorted(sarr,key=lambda k: k[1],reverse=True)
print("top scorers are ",sarr[0][0]," and ",sarr[1][0])
# print one more element here as a top scorer
marr=map(lambda x: x[1],sarr)
sum=reduce(lambda x,y: x+y,marr)
print("average student scores ",sum/n)

