import sys
from collections import deque

n, m, s, d, k = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    
for j in graph:
    j.sort()
    
def shortest_path(graph, s, d):
    que = deque()
    color = ["white"]*(n+1)
    parent = [None]*(n+1)
    path = []
    
    que.append(s)
    color[s] = "grey"
    while que:
        node = que.popleft()
        for i in graph[node]:
            if color[i] == "white":
                color[i] = "grey"
                parent[i] = node
                que.append(i)
            if i == d:
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

ans1 = shortest_path(graph, s, k)
ans2 = shortest_path(graph, k, d)
if ans1 == -1 or ans2 == -1:
    print(-1)
else:
    path = ans1 + ans2[1:]
    print(len(path) - 1)
    print(*path)    
            