n = str(int(input())+1)
for i in range(len(n)-1):
    print(end=n[i])
    if n[i] > n[i+1]:
        break
j=i+1
while j < len(n):
    print(end=n[i])
    j+=1
