p = int(input())
c = input()
s = ""

while p >= len(c):
    s += c[p%len(c)]
    p = p//len(c)-1
    
print(s+c[p])