import sys
import math

l = int(input())
h = int(input())
t = input()
abcs = []
for i in range(h):
    row = input()
    abcs.append(row)
    abcs[i] = list(map(''.join, zip(*[iter(abcs[i])]*l)))
print(abcs, file=sys.stderr)
for i in range(h):
    for j in range(len(t)):
        if t[j].isalpha():
            print(abcs[i][ord(t[j].upper())-ord('A')], end="") 
        else:
            print(abcs[i][26], end="")

    print("")
