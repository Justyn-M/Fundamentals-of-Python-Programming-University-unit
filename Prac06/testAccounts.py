#
# testAccounts.py
#

from accounts import *

accounts = []

bank = BankAccount('Everyday', '007', 2000)
accounts.append(bank)
bank = BankAccount('Cheque A/C', '008', 3000)
accounts.append(bank)
bank = BankAccount('Tem Deposit', '009', 20000)
accounts.append(bank)

balances(accounts)

print('\nDoing some transactions...\n')
accounts[0].deposit(100)
accounts[1].withdraw(500)
accounts[2].add_interest()

balances(accounts)
