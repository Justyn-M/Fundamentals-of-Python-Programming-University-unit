#
# numbers3.py: Read in a list of numbers (negative to exit) and give the sum of the numbers
#

count = 0
total = 0
print("Enter a list of numbers. negative to exit ")
number = int(input())

while number >= 0:
    count = count + 1
    #equivalent to count += 1
    total = total + number
    #equivalent to total += number
    print('Next Number ')
    number = int(input())

print('Total is ', total, ' and count is ', count)

