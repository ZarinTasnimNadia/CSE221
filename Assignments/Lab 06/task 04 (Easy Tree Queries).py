import sys
from collections import deque
sys.setrecursionlimit(2*100000+5)

n, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
q = int(sys.stdin.readline())
sub_size = [0]*(n+1)
color = ["white"]*(n+1)

def tree(u):
    color[u] = "grey" 
    size = 1
    
    for v in graph[u]:
        if color[v] == "white":
            size += tree(v)
    sub_size[u] = size        
    return size        
       
ans = tree(r)
for _ in range(q):
    x = int(sys.stdin.readline()) 
    print(sub_size[x])        