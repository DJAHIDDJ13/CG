import math
def make_diamond(lines):
    n = len(lines)
    diamond = []
    for i in range(2*n-1):
        x = n - abs(n-1-i)
        chars = []
        for j in range(x):
            #print(j + max(0, i-n+1), x-j-1 + max(0, i-n+1))
            chars.append(lines[j + max(0, i-n+1)][x-j-1 + max(0, i-n+1)])
        diamond.append(' '.join(reversed(chars)).center(2*n-1))
    return '\n'.join(''.join(row) for row in diamond)

size = int(input())
angle = int(input())
block = [input().split(' ') for _ in range(size)]

# rotate until the topmost corner of the diamond is at (0, 0)
for i in range((angle//90+1)%4):
    block = [line[::-1] for line in block]
    block = [line for line in zip(*block)]
print(make_diamond(block))
