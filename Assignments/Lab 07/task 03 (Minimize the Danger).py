import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
def dijkstra(graph):
    danger = [float("inf")]* (n+1)
    parent = [None] *(n+1)
    danger[1] = 0
    heap = [(0, 1)]
    visited = [False]*(n+1)
    
    while heap:
        c_danger, curr = heappop(heap)
        if visited[curr]:
                continue
        visited[curr] = True
        
        for v, w in graph[curr]:  
            max_danger = max(c_danger, w)
            if max_danger < danger[v]:
                danger[v] = max_danger
            
        
            # if c_danger < w:
            #     danger[v] = w
            # else:
            #     danger[v] = c_danger
            parent[v] = curr
            heappush(heap, (danger[v], v))             
                
    return danger


ans = dijkstra(graph)
for i in range(1, n+1):
    if ans[i] == float("inf"):
        ans[i] = -1
print(*ans[1::])
               