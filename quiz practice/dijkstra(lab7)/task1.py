import sys
from heapq import heappush, heappop

n, m, s, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    graph[u[i]].append((v[i], w[i]))
    
def dijkstra(graph, s, d):
    parent = [None]*(n+1)
    dist = [float("inf")]*(n+1)
    dist[s] = 0
    heap = [(0, s)]
    
    while heap:
        curr_d, node = heappop(heap)
        for v, w in graph[node]:
            distance = curr_d + w
            if distance < dist[v]:
                dist[v] = distance
                parent[v] = node
                heappush(heap, (distance, v))
                
    traversal = []
    current = d
    while current:
        traversal.append(current)
        current = parent[current]
        
    traversal.reverse()
    return dist, traversal                
    
dist, traversal = dijkstra(graph, s, d)

if dist[d] != float("inf"):
    print(dist[d])
    print(*traversal)
else:
    print(-1)        