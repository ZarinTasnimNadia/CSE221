import sys

n, m = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin. readline().split()))
v = list(map(int, sys. stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])
    
for j in graph:
    j.sort()
    
odd_degree = 0

for i in range(1, n+1):
    if len(graph[i]) % 2 != 0:
        odd_degree += 1

if odd_degree > 2:
    print("NO")
else:
    print("YES")    
                    