from numpy import convolve

n=int(input())
s=int(input())
c=[1]
for i in input().split():
    vi = int(i)
    p=[1]
    for j in range(0,n,vi):
        p+=[0]*(vi-1) + [1]
    c = convolve(c, p)

print(c[n])
