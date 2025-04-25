import sys

def has_cycle(n, adjlist):
    color = [0] * (n + 1)  
    def dfs(node):
        color[node] = 1  
        for neighbor in adjlist[node]:
            if color[neighbor] == 1:
                return True 
            if color[neighbor] == 0:
                if dfs(neighbor):
                    return True
        color[node] = 2  
        return False

    for i in range(1, n + 1):
        if color[i] == 0:
            if dfs(i):
                return True
    return False


n, m = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(2 * 100000 + 5)
adjlist = {i: [] for i in range(1, n + 1)}
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adjlist[u].append(v)

if has_cycle(n, adjlist):
    print("YES")
else:
    print("NO")
    
    
import sys
n, m = map(int, sys.stdin.readline().split())

adjlist = {i: [] for i in range(1, n+1)}
for j in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adjlist[u].append(v)



def colorr(adjlist, n):
    color = [0] * (n+1)
    flag = [False]
    for u in range(1, len(color)):
        if color[u] == 0:
            dfs(adjlist, color, u, flag) 
    if flag[0] == True:
        print("YES")
    else:
        print("NO")            
               

def dfs(adjlist, color, u, flag):
    
    color[u] = 1
    for v in adjlist[u]:
        if color[v] == 0:
            dfs(adjlist, color, v, flag)
        elif color[v] == 1:
            flag[0] = True
            break   
            
            
    color[u] = 2 
    return flag
    
colorr(adjlist, n)        

import sys
sys.setrecursionlimit(2*100000+5)

vertices, edges = map(int, input().split())
adlist = [[] for _ in range(vertices+1)]

# directed graph
for i in range(edges):
    oneEndpoint, anotherEndpoint = map(int, input().split())
    adlist[oneEndpoint].append(anotherEndpoint)

def has_cycle(graph, vertex, visited, rec_stack):
    visited[vertex] = True
    rec_stack[vertex] = True
    
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
            
    rec_stack[vertex] = False
    return False

def detect_cycle(graph, vertices):
    visited = [False] * (vertices + 1)
    rec_stack = [False] * (vertices + 1)
    
    for vertex in range(1, vertices + 1):
        if not visited[vertex]:
            if has_cycle(graph, vertex, visited, rec_stack):
                return True
    return False

if detect_cycle(adlist, vertices):
    print("YES")
else:
    print("NO")