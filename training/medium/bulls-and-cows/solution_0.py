from functools import partial
from collections import Counter

n = int(input())
inputs = [input().split() for _ in range(n)]
possible_guesses = [f"{i:04d}" for i in range(10000)]
def bulls_filter(guess, bulls, cows, elem):
    num_match_pos = sum([a == b for a, b in zip(elem, guess)])
    return num_match_pos == bulls and\
     sum((Counter(elem) & Counter(guess)).values()) - num_match_pos == cows
for guess, bulls, cows in inputs:
    bulls = int(bulls)
    cows = int(cows)
    possible_guesses = [*filter(partial(bulls_filter, guess, bulls, cows), possible_guesses)]
print(possible_guesses[0])