import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
length = n+1
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
diff = [0]*n

for i in range(m):
    graph[u[i]].append(v[i])
    diff[u[i] - 1] -= 1
    diff[v[i] - 1] += 1
    
for j in graph:
    j.sort()
    

print(*diff)            