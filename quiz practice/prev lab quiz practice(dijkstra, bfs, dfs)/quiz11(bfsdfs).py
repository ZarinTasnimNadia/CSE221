import sys
from collections import deque
from heapq import heappush, heappop

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])
for neighbors in graph:
    neighbors.sort()
    
def bfs(graph):
    cyan = set()
    red = set()
    track = [None]*(n+1)
    visited = [False]*(n+1)
    que = deque()
    
    for i in range(1, n+1):
        if not visited[i]:
            if not graph[i]:
                visited[i] = True
                track[i] = "A"
                continue
            
            visited[i] = True
            que.append(i)
            red.add(i)
            track[i] = "A"
        
            while que:
                node = que.popleft()
                
                for v in graph[node]:
                    if not visited[v]:
                        visited[v] = True
                        if track[node] == "A":
                            track[v] = "B"
                            cyan.add(v)
                        else:
                            track[v] = "A"
                            red.add(v)
                        que.append(v)
            
                    elif track[node] == track[v]:
                        return False
    return track[1:]

ans = bfs(graph)
if ans:
    print(*ans)  
else:
    print("X")                          