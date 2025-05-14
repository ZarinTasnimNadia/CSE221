import sys
from collections import deque
from heapq import heappop, heappush
sys.setrecursionlimit(2*100000+5)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
in_degree = [0]*n

for i in range(m):
    graph[u[i]].append(v[i])
    in_degree[v[i]] += 1
    
def dfs(graph):
    n = len(graph)
    color = ["white"]*n
    parent = ["white"]*n
    st = [(0, 0)]*n
    ft = [(0, 0)]*n
    traversal = []
    time = 0
    cycle = [False]
    
    def dfs_visit(u):
        nonlocal time
        traversal.append(u)
        color[u] = "grey"
        time += 1
        st[u] = (u, time)
        
        for v in graph[u]:
            if color[v] == "grey":
                cycle[0] = True
                
            if color[v] == "white":
                color[v] = "grey"
                parent[v] = u
                dfs_visit(v)
        color[u] = "black"
        time += 1
        ft[u] = (u, time)
    
    for u in range(len(graph)):
        if color[u] == "white":
            dfs_visit(u)
    ft = sorted(ft, key = lambda item: item[1], reverse = True)
    return ft, cycle[0]

def bfs(graph, in_degree):
    heap = []
    order = []
    in_degree = in_degree[:]
    
    for i in range(len(graph)):
        if in_degree[i] == 0:
            heappush(heap, -i)
    while heap:
        node = -heappop(heap)
        order.append(node)
        for v in graph[node]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heappush(heap, -v)   
                
    return order                 
        
res = bfs(graph, in_degree)
if len(res) == n:
    print(*res)
else:
    print(-1)       
    

ans, cycle = dfs(graph)
traversal = []
if cycle == False:
    for i in range(len(ans)):
        traversal.append(ans[i][0])
    print(*traversal)
else:
    print(-1)    
        
    


             
        
        
    
        