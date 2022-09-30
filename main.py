balance=0
def deposit(amount):
    global balance
    balance += amount
    return f"your balance {balance}"
def withdraw(amount):
    global balance
    balance -= amount
    return f"your balance {balance}"
class Money:
    def __init__(self,amount):
        self.amount=amount
money=Money(int(input("How much money do u want to deposite or withdraw: ")))
while(True):
    print("1 for add money")
    print("2 for withdraw")
    print("3 for exit")
    a=int(input())
    if (a==1):
        print(deposit(money.amount))
    elif(a==2):
        if(balance<=100):
            print("You dont have money")
        else:
            print(withdraw(money.amount))
    elif(a==3):
        break
    else:
        print("Please enter 1 or 2")


