n = int(input())

res = '' if n else '0'
while n:
    r = n % 3
    n = n // 3
    if r == 2:
        res = 'T' + res
        n += 1
    else:
        res = str(r) + res

print(res)