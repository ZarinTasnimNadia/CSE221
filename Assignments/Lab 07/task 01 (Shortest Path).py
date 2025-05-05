import sys
from heapq import heappush, heappop

n, m, s, d = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for i in range(m):
    graph[u[i]].append((v[i], w[i]))

def dijkstra(graph, s, d):
    
    dist = [float("inf")] * (n+1)    
    dist[s] = 0
    parent = [None]*(n+1)
    heap = [(0, s)]
    
    
    while heap:
        c_dist, curr = heappop(heap)
        if curr == d:
            break
        if c_dist > dist[curr]:
            continue
        for v, w in graph[curr]:
            distance = c_dist + w
            if dist[v] > distance:
                dist[v] = distance
                parent[v] = curr
                heappush(heap, (distance, v))
    
    
    if dist[d] == float("inf"):
        return -1, []
    else:
        path = []
        current = d
        
        while current != None:
            path.append(current)
            current = parent[current]
            
        path.reverse()
        return dist[d], path    

distance, path = dijkstra(graph, s, d)
print(distance)
print(*path)    
                
                
       