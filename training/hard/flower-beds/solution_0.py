import math
n = int(input())
coords = [tuple(map(int, input().split())) for _ in range(n)]
coords.append(coords[0]) # to complete the cycle

# https://en.wikipedia.org/wiki/Pick%27s_theorem
# => A = i + b / 2 - 1
# => i = A - b / 2 + 1
# we calculate A using https://en.wikipedia.org/wiki/Shoelace_formula
A = 0
b = 0
for p1, p2 in zip(coords, coords[1:]):
    A += p1[0] * p2[1] - p2[0] * p1[1]
    b += math.gcd(p1[0] - p2[0], p1[1] - p2[1])
A = A / 2

print(int(A - b/2 + 1))