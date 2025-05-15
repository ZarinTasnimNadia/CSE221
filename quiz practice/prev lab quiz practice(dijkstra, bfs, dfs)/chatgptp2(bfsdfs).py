import sys
from collections import deque
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

nodes = set(range(1, n+1))

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    #nodes.update([u, v])
    graph[u].append(v)

source = int(sys.stdin.readline().strip())    

def bfs(graph, source):
    visited = [False]*(n+1)
    que = deque()
    visited[source] = True
    que.append(source)
    traversal = set()
    
    while que:
        node = que.popleft()
        traversal.add(node)
    
        for v in graph[node]:
            if visited[v] == False:
                visited[v] = True
                que.append(v)
                
    return traversal ^ nodes

ans = bfs(graph, source)          
print(*ans)  
    