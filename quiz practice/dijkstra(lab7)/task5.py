import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for i in range(m):
    graph[u[i]].append((v[i], w[i]))
    
def dijkstra(graph):
    dist = [[float("inf"), float("inf")] for _ in range(n+1)]    
    dist[1][0], dist[1][1] = 0, 0
    heap = [(0, None, 1)]
    
    while heap:
        d, prev_p, node = heappop(heap)
        for v, w in graph[node]:
            distance = d + w
            parity = w % 2
            if prev_p == None or parity != prev_p:
                if distance < dist[v][parity]:
                    dist[v][parity] = distance
                    heappush(heap, (distance, parity, v))
            
    return min(dist[-1][0], dist[-1][1])

ans  = dijkstra(graph)
if ans == float("inf"):
    print(-1)
else:    
    print(ans)
            