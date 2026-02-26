class Car:
    wheels=4
    def drive(self):
        print("the car is moving")
jeep=Car()
print(jeep.wheels)
jeep.drive()

toyota=Car()
print(toyota.wheels)
toyota.drive()

class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} ksh has been successfully deposited your new balance is {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"{amount} ksh withdrawn.new balance is {self.balance}")

Account1=Account("john",1000)
Account1.deposit(500)
Account1.withdraw(700)

Account2=Account("mary",5000)
Account2.deposit(2000)
Account2.withdraw(10000)
        