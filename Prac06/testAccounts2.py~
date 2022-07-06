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

def balances():
    total = 0
    for i in range(len(accounts)):
        print('Name:', accounts[i].name, '\tNumber:', accounts[i].number,
                '\tBalance:', accounts[i].balance)
        total = total + accounts[i].balance
    print('\t\t\t\t\tTotal:', total)

#
# testAccounts.py
#

accounts = []

bank = BankAccount('Everyday', '007', 2000)
accounts.append(bank)
bank = BankAccount('Cheque A/C', '008', 3000)
accounts.append(bank)
bank = BankAccount('Tem Deposit', '009', 20000)
accounts.append(bank)
balances()

print('\nDoing some transactions...\n')
accounts[0].deposit(100)
accounts[1].withdraw(500)
accounts[2].add_interest()
balances()
