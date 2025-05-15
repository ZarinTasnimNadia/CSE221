import sys
from collections import deque
from heapq import heappop, heappush

n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n+1)]

pas = eval(sys.stdin.readline())

for u, v in pas:
   
    graph[u].append(v)
    
def dfs(graph):
    color = [0]*(n+1)
    parent = [None]*(n+1)
    cycle = [False]
    
    def dfs_visit(u):
        color[u] = 1
        for v in graph[u]:
            if color[v] == 1:
                cycle[0] = True
                return cycle[0]
            if color[v] == 0:
                color[v] = 1
                parent[v] = u
                dfs_visit(v)
                
        color[u] = -1
        
        
    for i in range(1, n+1):
        if color[i] == 0:
            dfs_visit(i)
    return cycle[0]

ans = dfs(graph)
print(ans)        