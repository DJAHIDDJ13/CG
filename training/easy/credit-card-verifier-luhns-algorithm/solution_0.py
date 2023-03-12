import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    card = ''.join(input().split())
    check = map(int, card[::-1][1::2])
    check = map(lambda x:x*2-9*(x>=5), check)
    check = sum(check)+sum(map(int, card[::-2]))
    print("NO" if check%10 else "YES")
