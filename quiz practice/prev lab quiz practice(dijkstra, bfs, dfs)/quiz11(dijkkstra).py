import sys
from collections import deque
from heapq import heappush, heappop

n, m, s, d, k = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for i in range(m):
    graph[u[i]].append((v[i], w[i]))
    graph[v[i]].append((u[i], w[i]))
    
def dijkstra(graph, s, d):
    dist = [float("inf")]*(n+1)
    parent = [None]*(n+1)
    dist[s] = 0
    heap = []
    heap.append((0, s))
    
    while heap:
        cur_d, u = heappop(heap)
        for v, w in graph[u]:
            distance = cur_d + w
            if distance < dist[v]:
                dist[v] = distance
                parent[v] = u
                heappush(heap, (distance, v))
    return dist[d]

dist1 = dijkstra(graph, s, k)
dist2 = dijkstra(graph, k, d)
if dist1 == float("inf") or dist2 == float("inf"):
    print(-1)
else:    
    print(dist1+dist2)            
        
