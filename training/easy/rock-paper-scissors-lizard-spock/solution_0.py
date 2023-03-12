import math
t = {"C": ['P','L'], "P":['R','S'], "R":['L','C'], "L":['S','P'], "S":['C','R']}
n = int(input())
h=[[]]
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    h[-1]+=[(numplayer,signplayer)]

for i in range(int(math.log(n, 2))):
    h+=[[]]
    for a,b in zip(h[-2][::2],h[-2][1::2]):
        win = a if a[0]<b[0] else b
        if b[1] in t[a[1]]:
            win = a
        if a[1] in t[b[1]]:
            win = b
        h[-1]+=[win]

champion = h[-1][0]
print(champion[0])
print(' '.join(reversed([str(h[i][h[i].index(champion)-1][0]) if h[i].index(champion)%2==1 else str(h[i][h[i].index(champion)+1][0]) for i in range(-2, -len(h)-1, -1)])))