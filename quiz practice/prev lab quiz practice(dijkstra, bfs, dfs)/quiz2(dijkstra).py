import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
s, d = map(int, sys.stdin.readline().split())

def dijkstra(graph, s, d):
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
    traversal = []
    current = d
    while current != None:
        traversal.append(current)
        current = parent[current]
        
    traversal.reverse()
    return dist[d], traversal 

dist, path = dijkstra(graph, s, d)
if dist == float("inf"):
    print("Impossible")
else:
    print("Time", dist)
    print("Route", end = " ")
    for j in range(len(path)-1):
        print(f"{path[j]}->", end = "" )
    print(path[-1])    
                       