# solution using algorithm from https://www.combinatorics.org/ojs/index.php/eljc/article/view/v12i1r27/pdf
# Essentially transforming the problem into a shortest path problem
# Or rather a graph diameter calculation, and solving it usign dijkstra

import heapq 
import math
from functools import reduce

def dijkstra(adj, source=0):
    INF = float('inf')

    dist = [0] * len(adj)
    prev = [0] * len(adj)
    PQ = []

    for v in range(len(adj)):
        if v != source:
            dist[v] = INF
            prev[v] = -1
        heapq.heappush(PQ, [INF, v])
    dist[source] = 0
    heapq.heappush(PQ, [0, source])
 
    while PQ:
        u_dist, u = heapq.heappop(PQ)

        if u_dist == dist[u]:
            for v, uv in enumerate(adj[u]):
                if uv > 0:
                    alt = dist[u] + uv
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        heapq.heappush(PQ, [alt, v])
    return dist

n = int(input())
nugget_portions = []
for i in range(n):
    nugget_portions += [int(input())]

nugget_portions = sorted(nugget_portions)
g = reduce(math.gcd, nugget_portions)

if g > 1:
    print("-1")
else:
    a1 = nugget_portions[0]
    graph = [[0 for _ in range(a1)] for _ in range(a1)]
    for u in range(a1):
        for v in range(a1):
            for k in range(n):
                if (u + nugget_portions[k]) % a1 == v:
                    graph[u][v] = nugget_portions[k]
                    break
    shortest_paths = dijkstra(graph, 0)
    graph_diameter = max(shortest_paths)
    nugget_num = graph_diameter - a1
    print(nugget_num)
