import sys
from heapq import heappush, heappop

n, m, s, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
def dijkstra(graph, s, d):
    dist = [[float("inf"), float("inf")] for _ in range(n+1)]    
    dist[s][0] = 0
    heap = [(0, s)]
    
    while heap:
        curr_d, node = heappop(heap)
        for v, w in graph[node]:
            distance = curr_d + w
            if distance < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = distance
                heappush(heap, (distance, v))
                
            elif dist[v][1] > distance > dist[v][0]:
                dist[v][1] = distance 
                heappush(heap, (distance, v))
                
    return dist[d][1]

ans = dijkstra(graph, s, d)  
if ans == float("inf"):
    print(-1)
else:
    print(ans)                     