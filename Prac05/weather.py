#
# weather.py: Print min and max temps from a file
#              (source: http://www.bom.gov.au/climate/)

import matplotlib.pyplot as plt

fileobj = open('marchweather.csv', 'r')
minline = fileobj.readline()
maxline = fileobj.readline()
fileobj.close()

minsplitline = minline.strip().split(',')
maxsplitline = maxline.strip().split(',')
print(minsplitline)
mins = [float(m) for m in minsplitline]
maxs = [float(m) for m in maxsplitline]

dates = [d for d in range(1,32)]

print(dates)

plt.plot(dates, mins, dates, maxs)
plt.title('March Weather')
plt.xlabel('Day')
plt.ylabel('Temp in Celsius')

plt.show()
