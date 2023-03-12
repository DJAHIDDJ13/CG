r1 = int(input())
r2 = int(input())
def suiv(n):
    return n + sum([int(i) for i in str(n)])
while r1 != r2:
    if r1<r2:
        r1 = suiv(r1)
    else:
        r2 = suiv(r2)
print(r1)
