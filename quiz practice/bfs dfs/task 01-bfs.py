import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for j in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for neighbours in graph:
    neighbours.sort()

def bfs(graph):
    que = deque()
    color = [0]* len(graph)
    traversal = []
    que.append(1)
    color[1] = 1
    
    while que:
        u = que.popleft()
        traversal.append(u)
        for i in graph[u]:
            if color[i] == 0:
                color[i] = 1
                que.append(i)
                
    return traversal


ans = bfs(graph)
print(*ans)             
    