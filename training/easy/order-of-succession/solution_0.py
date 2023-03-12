import sys
import math
from pprint import pprint
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
parents = {}
for i in range(n):
    name, parent, birth, death, religion, gender = input().split()
    birth = int(birth)
    
    info = {"name":name, 
            "parent":parent, 
            "birth":birth, 
            "death": death, 
            "religion": religion, 
            "gender": gender}
    if parent not in parents:
        parents[parent] = []
    parents[parent] += [info]
for parent in parents:
    parents[parent] = sorted(parents[parent], key=lambda p:[p['gender']=='F', p['birth']])

def DFS(parents, parent):
    if parent not in parents:
        return []
    retval = []
    for child in parents[parent]:
        retval += [child] + DFS(parents, child['name'])
    return retval

for succ in DFS(parents, '-'):
    if succ['death'] == '-' and succ['religion'] == 'Anglican':
        print(succ['name'])