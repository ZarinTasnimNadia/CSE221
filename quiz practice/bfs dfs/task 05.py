import sys
sys.setrecursionlimit(2*100000+5)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    
for j in graph:
    j.sort()
    
def cycle_detect(graph):
    color = ["white"] *(n+1)
    parent = [None]*(n+1)
    has_cycle =[False]
    
    def dfs_visit(u):
        color[u] = "grey"
        for v in graph[u]:
            if color[v] == "grey":
                has_cycle[0] = True
                return
            
            if color[v] == "white":
                color[v] = "grey"
                parent[v] = u
                dfs_visit(v)
                
            
        color[u] = "black"
         
    
    for u in range(1, len(graph)):
        if color[u] == "white":
            dfs_visit(u)
            
    return has_cycle[0]

ans = cycle_detect(graph)
if ans == False:
    print("NO")
else:
    print("YES")                            