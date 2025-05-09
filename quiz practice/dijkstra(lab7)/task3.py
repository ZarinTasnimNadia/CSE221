import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
def dijkstra(graph):
    dist = [float("inf")]*(n+1)
    dist[1] = 0
    heap = [(0, 1)]
    
    while heap:
        d, node = heappop(heap)
        for v, w in graph[node]:
            danger = max(d, w)
            if danger < dist[v]:
                dist[v] = danger
                heappush(heap, (danger, v)) 
                
    return dist

ans  = dijkstra(graph)
for i in range(1, n+1):
    if ans[i] == float("inf"):
        ans[i] = -1
print(*ans[1::])        
                               