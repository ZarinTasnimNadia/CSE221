import sys
from collections import deque
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]
for i in range(m):
    graph[u[i]].append(v[i])
    
def dfs(graph):
    n = len(graph)
    color = ["white"]*(n+1)
    parent = [None]*(n+1)
    st = [(0, 0)]*(n+1)
    ft = [(0,0)]*(n+1)
    time = 0
    cycle = [False]
    traversal = []
    path = []
    
    def dfs_visit(u, path):
        nonlocal time
        color[u] = "grey"
        time += 1
        traversal.append(u)
        path.append(u)
        st[u] = ((u, time))
        
        for v in graph[u]:
            if color[v] == "grey":
                cycle[0] = True
                cycle_st = path.index(v)
                return path[cycle_st:] + [v]
            if color[v] == "white":
                color[v] = "grey"
                parent[v] = u
                res = dfs_visit(v, path)
                if res:
                    return res
        color[u] = "black"
        time += 1
        ft[u] = (u, time) 
        path.pop()   
        
    for i in range(1, len(graph)):
        if color[i] == "white":
            res = dfs_visit(i, [])  
            if res:
                path = res
                break 
              
    return cycle[0], path, traversal

cycle, path, traversal = dfs(graph)
print(*traversal)
if cycle == False:
    print(0)
else:
    print(*path)    
print("-----------------------------------------------------------------")    


def dfs2(graph):
    n = len(graph)
    color = ["white"]*(n+1)
    parent = [None]*(n+1)
    time = 0
    st = [(0, 0)]*(n+1)
    ft = [(0, 0)]*(n+1)
    cycle = [False]
    traversal = []
    
    def dfs_visit2(u):
        nonlocal time
        time += 1
        st[u] = [(u, time)]
        color[u] = "grey"
        traversal.append(u)
        
        for v in graph[u]:
            if color[v] == "grey":
                cycle[0] = True
                #parent[v] = u
                point = v
                current = u
                path = []
                while current != point:
                    path.append(current)
                    current = parent[current]
                path.append(point) 
                path.reverse()
                path.append(path[0])
                return cycle[0], path   
                
            if color[v] == "white":
                color[v] = "grey"
                parent[v] = u
                res = dfs_visit2(v)
                if res:
                    return res
        time += 1
        ft[u] = (u, time)
        color[u] = "black"
        
    for i in range(1, len(graph)):
        if color[i] == "white":
            res = dfs_visit2(i)
            if res:
                return res
    

cycle, path = dfs2(graph)
if cycle == False:
    print(0)
else:
    print(*path)
                     
                
                
                