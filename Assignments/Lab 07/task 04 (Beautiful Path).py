import sys
from heapq import heappop, heappush

n, m, s, d = map(int, sys.stdin.readline().split())

w = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append((v, w[v-1]))

def dijkstra(graph, w, s, d):
    cost = [float("inf")]*(n+1) 
    cost[s] = w[s-1]
    heap = [(cost[s], s)]  
    
    while heap:
        cst, node = heappop(heap)
        
        for v, w in graph[node]:
            total = cst + w
            if total < cost[v]:
                cost[v] = total
                heappush(heap, (total, v))
                
    return cost[d] 

ans = dijkstra(graph, w, s, d)

if ans != float("inf"):
    print(ans)
else:
    print(-1)    

           