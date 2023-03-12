import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
players = [input() for i in range(n)]

cur_min_rounds = 10
winner = 0
for i in range(n):
    shoots = input().split()
    miss_count = 0
    score = 0
    num_rounds = 0
    num_shots = 0
    prev_total = 0
    for shot in shoots:
        if '*' in shot:
            score += eval(shot)
            miss_count = 0
        elif 'X' in shot:
            miss_count += 1
        else:
            score += int(shot)
            miss_count = 0
        
        if miss_count >= 1:
            score = max(score-20, 0)
        if miss_count >= 2:
            score = max(score-10, 0)
        if miss_count >= 3:
            score = 0
        
        num_shots += 1
        if num_shots == 3:
            num_shots = 0
            prev_total = score
            num_rounds += 1

        if score > 101:
            score = prev_total
            num_shots = 2

        if score == 101:
            break

    if cur_min_rounds > num_rounds:
        cur_min_rounds, winner = num_rounds, i
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(players[winner])
