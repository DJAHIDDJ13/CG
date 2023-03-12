import math
A, B = [int(i) for i in input().split()]
Y = int(input())
C, D = [int(i) for i in input().split()]
L = int(input())
W = int(input())
# time = SQRT((A - X) **2 + (B - Y) **2) / L + SQRT((C - X) ** 2 + (D - Y) **2 ) / W
# diff_time is the derivative of the above
diff_time = lambda X:(X - C) / (W * math.sqrt((C-X)**2+(D-Y)**2)) + (X - A) / (L * math.sqrt((A-X)**2+(B-Y)**2))
lo, hi = 0, 20_000_000
while hi - lo > 1:
    mid = (lo + hi) / 2
    if diff_time(mid) < 0:
        lo = mid
    else:
        hi = mid
print(int(hi))
