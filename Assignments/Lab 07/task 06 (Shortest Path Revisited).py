import sys
from heapq import heappush, heappop

n, m, s, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
def dijkstra(graph, s, d):
    dist1 = [float("inf")]*(n+1)
    dist2 = [float("inf")]*(n+1) 
    parent1 = [None]*(n+1)
    parent2 = [None]*(n+1)
    dist1[s] = 0
    heap = [(0, s)]
    
    while heap:
        curr_d, node = heappop(heap)
        for v, w in graph[node]:
            distance = curr_d + w
            if distance < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = distance
                parent1[v] = node
                heappush(heap, (distance, v))
                
            elif dist1[v] < distance < dist2[v]:
                dist2[v] = distance
                parent2[v] = node
                heappush(heap, (distance, v))
                
    return dist2[d]
    
    
ans = dijkstra(graph, s, d)
if ans == float("inf"):
    print(-1)
else:
    print(ans)                  
           
    