#
# bucket2.py - bucket list builder
#

print('\nBUCKET LIST BUILDER\n')

bucket = []

choice = input('Enter selection: e(X)it, (A)dd, (L)ist,(D)elete ')

while choice[0].upper() != 'X':
    if choice[0].upper() == 'A':
        print('Enter list item ')
        newitem = input()
        bucket.append(newitem)
    elif choice[0].upper() == 'L':
        for item in bucket:
            print(item)
    elif choice[0].upper() == 'D':
        del bucket[-1]
        print('Item Deleted')
    else:
        print('Invalid selection.')
    choice = input('Enter selection: e(X)it, (A)dd, (L)ist,(D)elete ')


print('\nGOODBYE!\n')
