n = str(int(input())+1)
i=0
for i in range(len(n)-1):
    print(end=n[i])
    if n[i] > n[i+1]:
        break
print(end=n[i]*(len(n)-i-1))
