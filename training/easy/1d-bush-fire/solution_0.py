import sys
import math
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    line = input().lstrip('.').rstrip('.')
    num_drops = 0
    j = 0
    while j < len(line):
        if line[j] == 'f':
            j += 3
            num_drops += 1
        else:
            j += 1
    print(num_drops)