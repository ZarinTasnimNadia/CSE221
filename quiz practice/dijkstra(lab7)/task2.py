import sys
from heapq import heappop, heappush

n, m, s, t = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    
def dijkstra(graph, s):
    dist = [float("inf")]*(n+1)
    parent = [None]*(n+1)
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


    return dist

alice = dijkstra(graph, s)
bob = dijkstra(graph, t)

min_time = float("inf")
node = -1

for i in range(1, n+1):
    if alice[i] != float("inf") and bob[i] != float("inf"):
        time = max(alice[i], bob[i])
        if time < min_time or (time == min_time and i < node):
            min_time = time
            node = i

if min_time == float("inf"):
    print(-1)
else:
    print(min_time, node)    
                
    