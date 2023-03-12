import sys
import math
import random
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
edges = [[] for _ in range(n)]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    edges[n1].append(n2) 
    edges[n2].append(n1)
print(edges, file=sys.stderr)
exits = []
def sever(s, e):
    print(s,e,edges, file=sys.stderr)
    print(s, e)
    edges[s].remove(e)
    edges[e].remove(s)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    found = False
    for i in edges[si]:
        if i in exits:
            sever(i, si)
            found = True
    if not found:
        ran = random.randint(0,n-1)
        while len(edges[ran]) == 0:
            ran = random.randint(0,n-1)
        sever(ran, random.choice(edges[ran]))
