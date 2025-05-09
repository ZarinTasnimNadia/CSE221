import sys
from heapq import heappop, heappush

n, m, s, d = map(int, sys.stdin.readline().split())

w = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append((v, w[i]))
print(graph)    