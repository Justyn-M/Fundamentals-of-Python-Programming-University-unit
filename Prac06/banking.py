#
# banking.py
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

choice = input('Enter transaction type: (W/D/I/B) X to exit: ')

while choice.upper() != 'X':
    if choice.upper() == 'W':
        achoice = int(input('Which account ? (0-'+ str(len(accounts)-1) + ')'))
        amount = int(input('Amount to withdraw: '))
        accounts[achoice].withdraw(amount)
    elif choice.upper() == 'D':
        achoice = int(input('Which account ? (0-'+ str(len(accounts)-1) + ')'))
        amount = int(input('Amount to deposit: '))
        accounts[achoice].deposit(amount)
    elif choice.upper() == 'I':
        achoice = int(input('Which account ? (0-'+ str(len(accounts)-1) + ')'))
        accounts[achoice].add_interest()
    elif choice.upper() == 'B':
        achoice = int(input('Which account ? (0-'+ str(len(accounts)-1) + ')'))
        print('Balance: ', accounts[achoice].balance)

    else:
        print('Invalid Transaction')
    choice = input('Enter transaction type: (W/D/I/B) X to exit: ')

balances(accounts)

