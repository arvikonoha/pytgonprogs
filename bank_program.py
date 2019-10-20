class bank_account:
    def __init__(self, account_no, balance=100):
        self.__account_no = account_no
        self.__balance = float(balance)

    def deposit(self, amount):
        self.__balance += float(amount)
        print("Balance after deposit ", self.__balance)

    def withdraw(self, amount):
        if (self.__balance - float(amount)) < 100:
            print("Insuffient funds")
        else:
            self.__balance -= float(amount)
            print("Balance after withdraw ", self.__balance)

    def getbalance(self):
        return self.__balance

    def getaccno(self):
        return self.__account_no


def check_accno(lst, acc_no):
    for i in lst:
        if i.getaccno() == acc_no:
            return True
        else:
            return False


def getacc(lst, acc_no):
    for i in lst:
        if check_accno(lst, acc_no):
            return i
    return None


lst = []

while True:
    choice = input(
        "Enter your choice (create,deposit,withdraw,get_top_account,exit) ")
    if choice == "create":
        account_no = input("Enter your account no ")
        if check_accno(lst, account_no):
            print("Account number already exists")
        else:
            balance = input("Enter the balance")
            lst.append(bank_account(account_no, balance))
    elif choice == "deposit":
        amount, account_no = input("Enter the amount to deposit "), input(
            "Enter the account number ")
        if not check_accno(lst, account_no):
            print("Account doesn't exist")
        else:
            account = getacc(lst, account_no)
            account.deposit(amount)
    elif choice == "withdraw":
        amount, account_no = input("Enter the amoun to withdraw "), input(
            "Enter the account number ")
        if not check_accno(lst, account_no):
            print("Account doesn't exist")
        else:
            account = getacc(lst, account_no)
            account.withdraw(amount)
    elif choice == "get_top_account":
        lst = sorted(lst, key=bank_account.getbalance, reverse=True)
        if len(lst) > 0:
            print("Account Number with most balance ", lst[0].getaccno(),
                  lst[0].getbalance())
        else:
            print("There are no accounts")
    elif choice == "exit":
        break
    else:
        print("Invalid choice")
