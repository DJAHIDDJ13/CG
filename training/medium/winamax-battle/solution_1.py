import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
p1,p2=[],[]

c2n={**{i:int(i) for i in [str(i) for i in range(2,11)]},**{'J':11,'Q':12,'K':13,'A':14}}
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    p1+=[cardp_1]

m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    p2+=[cardp_2]

rounds=0
tie=False
while len(p1)!=0 and len(p2)!=0:
    bid1 = [p1.pop(0)]
    val1=bid1[0]
    bid2 = [p2.pop(0)]
    val2=bid2[0]
    while c2n[val1[:-1]]==c2n[val2[:-1]]:
        for i in range(3):
            if len(p1)==0 or len(p2)==0:
                tie=True
                break
            bid1.append(p1.pop(0))
            bid2.append(p2.pop(0))
        if tie:
            break
        if len(p1)==0 or len(p2)==0:
            tie=True
            break
        val1=p1.pop(0)
        val2=p2.pop(0)
        bid1.append(val1)
        bid2.append(val2)
    if tie:
        break
    if c2n[val1[:-1]]>c2n[val2[:-1]]:
        p1=p1+bid1+bid2
    elif c2n[val1[:-1]]<c2n[val2[:-1]]:
        p2=p2+bid1+bid2
    rounds+=1
if tie:
    print('PAT')
elif len(p1)==0:
    print(2,rounds)
elif len(p2)==0:
    print(1,rounds)
