n = int(input())
combs = []
for tries in range((n//5)+1):
    for transforms in range(tries+1):
        total = tries * 5 + transforms * 2
        remainder = n - total
        if remainder % 3 == 0 and remainder >= 0:
            penalties = remainder // 3
            combs += [(tries, transforms, penalties)]
            
combs = sorted(combs, key=lambda x:[x[0], x[1], x[2]])
for a,b,c in combs:
    print(a,b,c)