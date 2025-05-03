import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for x in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# red = set()

# cyan = set()

# que = deque()
color = ["white"]*(n+1)
bip = True
track = [None]*(n+1)
total_max = 0

for u in range(1, n+1):
    if color[u] == "white":
        if not graph[u]:
            # Isolated node — can go in either set
            total_max += 1
            color[u] = "black"
            continue
        red = set()
        cyan = set()
        que = deque()
        que.append(u)
        red.add(u)
        track[u] = "red"
        color[u] = "grey"
            
        while que:
            node = que.popleft()
            # if parent[node] == "cyan":
            #     red.add(node)
                
            # if parent[node] == "red":
            #     cyan.add(node)
            for v in graph[node]:
                if color[v] == "white":
                    color[v] = "grey"
                    que.append(v)
                    if track[node] == "red":
                        #parent[v] = "red"
                        cyan.add(v)
                        track[v] = "cyan"
                        
                    else:
                        #parent[v] = "cyan"
                        red.add(v)
                        track[v] = "red"
                        
                else:
                    if track[v] == track[node]:
                        bip = False
            
                        
            color[node] = "black"          
        total_max += max(len(red), len(cyan))      
                               

if bip == True:
    print(total_max)
else:
    print("conflict")   
    
     




