import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

size = int(input())

scores = {}
n = int(input())
for i in range(n):
    name = input()
    scores[name] = 0

t = int(input())
for i in range(t):
    inputs = input().split()
    throw_name = inputs[0]
    throw_x = int(inputs[1])
    throw_y = int(inputs[2])

    radius = size / 2
    manhattan_dist = abs(throw_x) + abs(throw_y)
    if manhattan_dist <= radius:
        scores[throw_name] += 15
    else:
        euclidian_dist_sqr = throw_x**2 + throw_y**2
        if euclidian_dist_sqr < radius*radius:
            scores[throw_name] += 10
        elif abs(throw_x) <= radius and abs(throw_y) <= radius:
            scores[throw_name] += 5

scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)

for name, score in scores:
    print(name, score)