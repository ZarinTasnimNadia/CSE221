import sys
from heapq import heappop, heappush

n, m, l, s, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
inp = []

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    inp.append([u, v, w])
    
def dijkstra(graph, s, d):
    dist = [float("inf")]*(n+1)
    parent = [None]*(n+1)
    dist[s] = 0
    heap = [(0, s)]
    
    while heap:
        curr_d, node = heappop(heap)
        for v, w in graph[node]:
            distance = w + curr_d
            if distance < dist[v]:
                dist[v] = distance
                parent[v] = node
                heappush(heap, (distance, v))
                
    return dist[d]
ans = dijkstra(graph, s, d)
if ans == float("inf"):
    print("NO")
else:
    dist = l - ans
    print("YES")
    for i in range(len(inp)):
        if inp[i][2] == 0:
            inp[i][2] = dist
        print(*inp[i])            

            

    

    