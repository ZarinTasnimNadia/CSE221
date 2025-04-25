import sys
n, m, s, d = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys. stdin.readline().split()))

adjlist = {i : [] for i in range(1, n+1)}

for j in range(m):
    adjlist[u[j]].append(v[j])
    adjlist[v[j]].append(u[j])
    
for neighbours in adjlist.values():
    neighbours.sort()
    
q = []
color = [0] * (n+1)
parent = [None] * (n+1)
path = []

q.append(s)
color[s] = 1
while q: 
    node = q.pop(0)
    for value in adjlist[node]:
        if color[value] != 1:
            color[value] = 1
            parent[value] = node
            q.append(value)
        if value == d:
            break    
if parent[d] == None and s != d:
    print(-1)            
else:    
    path.append(d)
    while True:
        if parent[d] == None:
            break
        path.insert(0, parent[d])
        d = parent[d]
    print(len(path) - 1)    
    print(*path)    