import sys
from collections import deque

n, m, s, d = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

graph = [[] for i in range(n+1)]

for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])
    
for j in graph:
    j.sort()    

def shortest_path(graph, s, d):
    color = ["white"]*(n+1)
    parent = [None]*(n+1)
    que = deque()
    path = []
    
    color[s] = "grey"
    que.append(s)
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

path = shortest_path(graph, s, d)  
if path == -1:
    print(path)
else:              
    print(len(path) - 1)
    print(*path)
                   
                    
        
    
    
    