import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
 
def bfs(node, graph):
    dist = [float("-inf")] * (n+1)
    dist[node] = 0
    que = deque()
    que.append(node)
    
    while que:
        u = que.popleft()
        for v in graph[u]:
            if dist[v] == float("-inf"):
                dist[v] = dist[u] + 1
                que.append(v)
                
    a, b = node, dist.index(max(dist))
    return a, b, dist[b], dist

a, b, d1, dist1 = bfs(1, graph)

x, y, d2, dist2 = bfs(b, graph)   

print(d2)
print(b, y)   
          
        

        
