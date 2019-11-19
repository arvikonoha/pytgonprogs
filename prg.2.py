bs=float(input("enter the basic salary "))
allow=float(input("enter the allowance "))
grosspay = bs+allow
if grosspay <= 5000:
	netpay = grosspay
	it = 0
elif grosspay>500 and grosspay<=10000:
	netpay = grosspay * .9
	it = grosspay * .1
elif grosspay > 10000 and grosspay <=20000:
	netpay = grosspay*.8
	it = grosspay*.2
else:
	netpay = grosspay * .7
	it=grosspay*.3
print("basic salary ",bs)
print("allowance ",allow)
print("gross pay ",grosspay)
print("net pay ",netpay)
print("income tax ",it)
