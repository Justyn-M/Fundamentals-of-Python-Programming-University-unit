#
# bucket1.py - use a python list for items in a bucket list
#

print('\nBUCKET LIST\n')

bucket1 = ['Witness something truly majestic', 'Help a complete stranger', 'Laugh until I cry', 'Drive a Shelby Mustang']

bucket1.append('Kiss the most beautiful girl in the world')
bucket1.append('Get a tattoo')
bucket1.append('Skydiving')
del bucket1[5]

bucket2 = ['Visit Stonehenge', 'Drive a motorcycle on the Great Wall of China', 'Go on a Safari', 'Visit the Taj Mahel', 'Sit on the Great Egyptian Pyramids', 'Find the Joy in your life']

print('Bucket 1: ', bucket1)
print('Bucket 2: ', bucket2)
bucket = bucket1 + bucket2
bucket.insert(5, 'Get a tattoo')

print('Joined buckets: ', bucket)

print('\nNicer formatting \n')

for item in bucket:
    print(item)

