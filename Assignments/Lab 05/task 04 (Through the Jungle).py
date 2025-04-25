import sys
n, m, s, d, k = map(int, sys.stdin.readline().split())

adjlist = {i : [] for i in range(1, n+1)}

for j in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adjlist[u].append(v)

for neighbours in adjlist.values():
    neighbours.sort()
    
def bfs(adjlist, s, d):
    
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
        return -1
    else:
        path.append(d)
        while True:
            if parent[d] == None:
                break 
            path.insert(0, parent[d])
            d = parent[d]
            
        return path
    
s2k = bfs(adjlist, s, k)
k2d = bfs(adjlist, k, d)

if s2k == -1 or k2d == -1:
    print(-1)
else:
    path = s2k + k2d[1::]
    print(len(path) - 1)
    print(*path)                       