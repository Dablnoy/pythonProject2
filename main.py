# balance=0
# def deposit(amount):
#     global balance
#     balance += amount
#     return f"your balance {balance}"
# def withdraw(amount):
#     global balance
#     balance -= amount
#     return f"your balance {balance}"
# class Money:
#     def __init__(self,amount):
#         self.amount=amount
# money=Money(int(input("How much money do u want to deposite or withdraw: ")))
# while(True):
#     print("1 for add money")
#     print("2 for withdraw")
#     print("3 for exit")
#     a=int(input())
#     if (a==1):
#         print(deposit(money.amount))
#     elif(a==2):
#         if(balance<=100):
#             print("You dont have money")
#         else:
#             print(withdraw(money.amount))
#     elif(a==3):
#         break
#     else:
#         print("Please enter 1 or 2")
#

# task 2
class Money:
    def __init__(self,amount,number,currency):
        self.number=number
        self.amount=amount
        self.currency=currency

    def to_tenge(self):
        if(self.currency=="USD"):
           return self.amount*self.number*476.39
        elif(self.currency=="EURO"):
            return self.amount*self.number*464.81
        elif(self.currency=="RUB"):
            return self.amount*self.number*7.91
        else:
            print("Incorrect currency, please delete it ")


    def get(self):
        return f'{self.amount} of {self.number} {self.currency}'

class Wallet():
    def __init__(self,mon):
        self.money=[]
        self.money.append(Money.get(mon))
    def addToWallet(self,mon):
        self.money.append(Money.get(mon))
    def getByIndex(self,a):
       print(self.money[a])

    def delbyIndex(self,b):
        self.money[b]

    def size(self):
        for name in range(len(self.money)):
            print(f'index: {name} FOR {self.money[name]}')
    def __str__(self):
         return self.money

a=Money(5,10,"USD")
b=Money(3,10,"EURO")
c=Money(150,10,"RUB")
m=Wallet(a)
m.addToWallet(b)
m.addToWallet(c)
print(m.__str__())
m.size()
c=[a.to_tenge(),b.to_tenge(),c.to_tenge()]
print(f'Сумма {sum(c)}')












