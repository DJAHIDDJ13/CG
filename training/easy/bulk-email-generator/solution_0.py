import sys
import re

n = int(input())
mail = sys.stdin.read()

rand = 0
def choose_rand(match):
    global rand
    choices = match.group(1).split('|')
    rand_choice = choices[rand%len(choices)]
    rand+=1
    return rand_choice

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(re.sub(r'\((.*?)\)', choose_rand, mail, flags=re.DOTALL))
