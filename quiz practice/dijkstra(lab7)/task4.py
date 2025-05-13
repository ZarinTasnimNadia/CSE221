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
    heap = [(w[s-1], s)]
    cost[s] = w[s-1]
 
    while heap:
        curr_cost, curr = heappop(heap)
        if curr_cost > cost[curr]:
            continue
        for v, w in graph[curr]:
            c = curr_cost + w
            if c < cost[v]:
                cost[v] = c
                heappush(heap, (c, v))
    return cost
 
ans = dijkstra(graph, w, s, d)
           
if ans[d] == float("inf"):
    print(-1)
else:
    print(ans[d])    

    
