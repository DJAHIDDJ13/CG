import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

_input = input()
states = input()
number_of_transitions = int(input())
T = {}
for i in range(number_of_transitions):
    A,a,B = input().split()
    T[f'{A} {a}'] = B
start_state = input()
end_states = input().split()
number_of_words = int(input())
for i in range(number_of_words):
    word = input()

    state = start_state
    err = False
    for c in word:
        try:
            state = T[f'{state} {c}']
        except:
            err = True
            break
    if state in end_states and not err:
        print('true')
    else:
        print('false')

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
