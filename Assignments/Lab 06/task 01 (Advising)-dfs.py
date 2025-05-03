import sys
from collections import deque
sys.setrecursionlimit(2*100000+5)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for x in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    
def dfs(graph, n):
    color = ["white"]*(n+1)
    parent = [None]*(n+1)
    time = 0
    st = [(0, 0)]*(n+1)
    ft = [(0, 0)]*(n+1)
    cycle = [False]
    
    def dfs_visit(u):
        nonlocal time
        color[u] = "grey"
        time += 1
        st[u] = (u, time)
        for v in graph[u]:
            if color[v] == "grey":
                cycle[0] = True
                
            if color[v] == "white":
                parent[v] = u
                dfs_visit(v)
        color[u] = "black"
        time += 1
        ft[u] = (u, time)       
    
    for u in range(len(color)):
        if color[u] == "white":
            dfs_visit(u)
    ft = sorted(ft, key = lambda item: item[1], reverse = True)
    
    ans = []
    if cycle[0] == True:
        ans.append(-1) 
        return ans
    
    for i in ft[0:-1]:
        ans.append(i[0])
    return ans        

ans = dfs(graph, n)    
print(*ans)

  
   
        
        
