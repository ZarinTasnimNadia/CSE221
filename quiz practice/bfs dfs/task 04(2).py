import sys
from collections import deque
n, m, s, d, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    
for j in graph:
    j.sort()
    
def bfs(graph, s, d):
    color = ["white"]*(len(graph))
    parent = [None] *(len(graph))        
    que = deque()
    que.append(s)
    color[s] = "grey"
    path = []
    
    while que:
        node = que.popleft()
        
        for v in graph[node]:
            if color[v] == "white":
                color[v] = "grey"
                parent[v] = node
                que.append(v)
            if v == d:
                break
    if parent[d] == None and s != d:
        return -1
    else:
        path.append(d)
        while True:
            if parent[d] == None:
                break
            path.insert(0, parent[d])
            d = parent[d]
            
    return path


ans1 = bfs(graph, s, k)    
ans2 = bfs(graph, k, d)

if ans1 == -1 or ans2 == -1:
    print(-1)
else:
    path = ans1 + ans2[1:]
    print(len(path) -1)
    print(*path)         
                            
        