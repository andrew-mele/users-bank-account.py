class BankAccount:
    accounts = []

    def __init__(self, intRate, balance):
        self.intRate = intRate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('Insufficient Funds: Charging a $5 fee')
            self.balance -= 5
            print(f'New balance after 5$ fee: {self.balance}')
        return self

    def displayAccountInfo(self):
        print(f'Your current balance is: ${self.balance} USD')
        return self

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += self.balance * self.intRate
        return self


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(.03, 3000)

    def checkAccountInfo(self):
        self.account.displayAccountInfo
        print(f'Hello, {andrew.name}, Your current balance is: ${self.account.balance} USD')
        return self


andrew = User('Andrew')

andrew.checkAccountInfo().account.withdraw(1433).deposit(230)

andrew.checkAccountInfo()
