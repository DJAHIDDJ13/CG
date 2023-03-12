n = int(input())
x = input()
a = sorted(list(map(int, input().split())))
print(a[-1] - a[0] + max(a[0], n-a[-1]))