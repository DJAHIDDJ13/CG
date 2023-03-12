import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rounds = int(input())
cash = int(input())
for i in range(rounds):
    ball, call, *num = input().split()
    ball = int(ball)
    bet = math.ceil(cash / 4)

    if call == 'PLAIN':
        cash += (35*bet if ball == int(num[0]) else -bet)
    else:
        if call == 'ODD':
            cash += bet if ball % 2 else -bet
        else:
            cash += -bet if ball % 2 or ball == 0 else bet

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(cash)
