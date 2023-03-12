c = complex(input().replace('i','j'))
m = int(input())

f = 0
i = 1
while i < m:
    f = f**2 + c
    if abs(f) >= 2:
        break
    i+=1

print(i)