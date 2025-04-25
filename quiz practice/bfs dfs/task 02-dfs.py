import sys
sys.setrecursionlimit(2*100000+5)

n, m = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

graph = [[] for i in range(n+1)]

for j in range(m):
    graph[u[j]].append(v[j])
    graph[v[j]].append(u[j])
    
for neighbours in graph:
    neighbours.sort()
    
def dfs(graph):
    n = len(graph)
    color = ["white"]* (n)
    parent = [None]*(n)
    ts = [None]*n
    tf = [None]*n
    traversal = []
    time = 0
            
    def dfs_visit(u):
        nonlocal time
        traversal.append(u)
        color[u] = "grey"
        time += 1
        ts[u] = time 
        for v in graph[u]:
            if color[v] == "white":
                parent[v] = u
                dfs_visit(v)
        color[u] = "black"
        time += 1
        tf[u] = time           
    
    for u in range(1, len(color)):
        if color[u] == "white":
            dfs_visit(u)
    return traversal            
        
ans = dfs(graph)
print(*ans)        
    
    
    
            