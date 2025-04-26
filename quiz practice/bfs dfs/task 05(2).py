import sys
sys.setrecursionlimit(2*100000+5)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    
for j in graph:
    j.sort()
    
def cycle_detect(graph):
    length = len(graph)   
    color = ["white"]* length
    parent = [None]* length
    cycle = [False]
    
    def dfs_visit(u):
        color[u] = "grey"
        for v in graph[u]:
            if color[v] == "grey":
                cycle[0] = True
                break
            if color[v] == "white":
                color[v] = "grey"
                parent[v] = u
                dfs_visit(v)
                
        color[u] = "black"        
    
     
    for u in range(1, length):
        if color[u] == "white":
            dfs_visit(u)     
            
    return cycle[0]


ans = cycle_detect(graph)
if ans == False:
    print("NO") 
else:
    print("YES")           