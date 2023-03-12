import sys
def suiv(n):
    return n + sum([int(i) for i in str(n)])
r = int(input())
c = 0
s=0
for i in range(max(0,r-9*len(str(r))), r):
    s +=1
    if suiv(i) == r:
        c+=1
print("YES" if c>0 else "NO")
