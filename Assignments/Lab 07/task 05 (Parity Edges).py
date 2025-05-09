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
    parent = [[None, None]]*(n+1)
    dist[1][0] = 0
    dist[1][1]
    heap = [(0, None, 1)]
    
    while heap:
        curr_d, prev_d, curr = heappop(heap)
        for v, w in graph[curr]:
            distance = curr_d + w
            if prev_d == None or ((prev_d % 2 == 0 and w % 2 != 0) or (prev_d % 2 != 0 and w % 2 == 0)):
                if distance < dist[v][w%2]:
                    dist[v][w%2] = distance
                    parent[v][w%2] = curr
                    heappush(heap, (distance, w, v))
                
    return min(dist[-1][0], dist[-1][1])

ans  = dijkstra(graph)
if ans == float("inf"):
    print(-1)
else:
    print(ans)    
    
       
    