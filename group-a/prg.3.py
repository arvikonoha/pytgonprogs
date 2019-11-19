def fibo(n):
        f1=0
        f2=1
        f3=0
        for i in range(0,n):
                print(f1,end=" ")
                f3=f1+f2
                f1=f2
                f2=f3

n=int(input("enter the value of n "))
print("fibonacci numbers upto ",n,"th term ")
fibo(n)

