import sys
from heapq import heappush, heappop

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]

u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    graph[u[i]].append((v[i], w[i]))
    
def dijkstra(graph):
    dist = [[] for _ in range(n)]
    parent = [None]*(n)
    heap = [(0, 0, [0])] 
     
    
    while heap:
        curr_d, node, path = heappop(heap)
        dist[node].append((curr_d, path))
        for v, w in graph[node]:
            if len(dist[v]) < 2:
                distance = w + curr_d
                heappush(heap, (distance, v, path + [v]))
                
    if len(dist[1]) < 2:
        return [-1]
    else:
        return dist[1][1][1]
        
ans = dijkstra(graph)
print(*ans)                    