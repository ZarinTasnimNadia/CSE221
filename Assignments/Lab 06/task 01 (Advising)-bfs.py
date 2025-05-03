import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adjlist = [[] for x in range(n+1)]
in_degree = [0]*(n+1)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adjlist[u].append(v)
    in_degree[v] += 1
    
que = deque()
order = []    

for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        que.append(i)
        
while que:
    node = que.popleft()
    order.append(node)
    
    for j in adjlist[node]:
        in_degree[j] -= 1
        if in_degree[j] == 0:
            que.append(j)        
            
if len(order) == n:
    print(*order) 
else:
    print(-1)           
    
    