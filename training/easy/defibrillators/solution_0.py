import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
lon = float(lon[:lon.index(',')] + '.' + lon[lon.index(',')+1:])
lat = float(lat[:lat.index(',')] + '.' + lat[lat.index(',')+1:])

dataString = ""
for i in range(n):
    defib = input()
    dataString += defib
data = []
for i in range(1,1+n*5,5):
    data.append(dataString.split(';')[i:i+5])
for i in range(n):
    data[i][4] = float(data[i][4][:data[i][4].index(',')] +'.'+data[i][4][data[i][4].index(',')+1:])
    data[i][3] = float(data[i][3][:data[i][3].index(',')] +'.'+data[i][3][data[i][3].index(',')+1:])
distances = []
for i in range(n):
    x = (data[i][3]-lon) * math.cos((lat+data[i][4])/2)
    y = data[i][4] - lat
    distances.append(math.sqrt((x**2)+(y**2)))
ind = 0;
for i in range(1,n):
    if(distances[ind]>distances[i]):
        ind = i

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(data[ind][0])
