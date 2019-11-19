paypweek = float(input("enter the pay rate per week "))
hourspweek = int(input("enter the hours worked per week "))
noofweeks=int(input("enter the number of weeks for the required month "))
def monthlypay(ppw,now,noh):
	return ppw*now*noh
print("Monthly pay ",monthlypay(paypweek,noofweeks,hourspweek))

