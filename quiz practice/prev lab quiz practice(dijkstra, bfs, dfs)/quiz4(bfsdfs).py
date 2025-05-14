import sys
from collections import deque
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
w = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append((v, w[v-1]))
    graph[v].append((u, w[u-1]))

def dfs(graph, w):
    n = len(graph)
    color = ["white"]*(n+1)
    parent = [None]*(n+1)
    st = [(0, 0)]*(n+1)
    ft = [(0, 0)]*(n+1)
    cycle = [False]
    time = 0
    gold = [0]*(n+1)
    gold[1] = w[0]
    
    def dfs_visit(u):
        nonlocal time
        color[u] = "grey" 
        time += 1
        st[u] = (u, time)
        
        for v, g in graph[u]:
            if color[v] == "white":
                color[v] = "grey"
                parent[v] = u
                gold[v] = g + gold[u]
                
                dfs_visit(v)       
        color[u] = "black"
        time += 1
        ft[u] = (u, time)
    for i in range(1, len(graph)):
        if color[i] == "white":
            dfs_visit(i)    
    return max(gold[1:])

def bfs(graph, w):
    que = deque()
    color = ["white"]*(n+1)
    gold = [0]*(n+1)
    que.append(1)
    color[1] = "grey"
    gold[1] = w[0]
    
    while que:
        node = que.popleft()
        for v, g in graph[node]:
            if color[v] == "white":
                color[v] = "grey"
                gold[v] = g + gold[node]
                que.append(v)
    return max(gold[1:])                
            
    
res = bfs(graph, w)
print("bfs:",res)    



ans = dfs(graph, w)
print("dfs:", ans)        