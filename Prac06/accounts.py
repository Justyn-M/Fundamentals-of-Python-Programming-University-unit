#
# accounts.py
#

class BankAccount():
    interest_rate = 0.03
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

def balances(acc):
    total = 0
    for i in range(len(acc)):
        print('Name:', acc[i].name, '\tNumber:', acc[i].number, 
                '\tBalance:', acc[i].balance)
        total = total + acc[i].balance
    print('\t\t\t\t\tTotal:', total)


