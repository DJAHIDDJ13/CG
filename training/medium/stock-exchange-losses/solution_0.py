import sys
import math
n = int(input())
v = []
for i in input().split():
    val = int(i)
    v.append(val)
current_min = 0
current_max = 0
max_loss = 0
for j in range(n):
    value = int(v[j])
    if value > current_max:
        if current_max - current_min > max_loss:
            max_loss = current_max - current_min
        current_max = value
        current_min = value
    elif value < current_min:
        current_min = value

    if current_max - current_min > max_loss:
        max_loss = current_max - current_min
print(-max_loss)