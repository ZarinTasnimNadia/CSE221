import sys
from heapq import heappop, heappush

n, m, s, t = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    
def dijktra(graph, s):
    dist = [float("inf")] * (n+1)
    parent = [None]*(n+1)
    heap = [(0, s)]
    dist[s] = 0
    
    while heap:
        c_dist, curr = heappop(heap)
        if c_dist > dist[curr]:
            continue
        for v, w in graph[curr]:
            distance = c_dist + w
            if dist[v] > distance:
                dist[v] = distance
                parent[v] = curr
                heappush(heap, (distance, v))
                
    return dist
                
        
alice = dijktra(graph, s)
bob = dijktra(graph, t)

min_time = float("inf")
node = -1

for j in range(1, n+1):
    if alice[j] != float("inf") and bob[j] != float("inf"):
        time = max(alice[j], bob[j])
        if time < min_time or (time == min_time and j < node):
            min_time = time
            node = j
            
if min_time == float("inf") and node == -1:
    print(-1)
else:
    print(min_time, node)                
                 