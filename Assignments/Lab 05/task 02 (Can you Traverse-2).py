import sys
n, m = map(int, sys.stdin.readline().split())

adjlist = {i : [] for i in range(1, n+1)}


u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
    
for j in range(m):
    adjlist[u[j]].append(v[j])
    adjlist[v[j]].append(u[j])
    
for values in adjlist.values():
    values.sort(reverse=True)    

stack = []
traversal = []
color = [0]* (n+1)

stack.append(1)
while stack:
    node = stack.pop()
    if color[node] != 1:
        color[node] = 1
        traversal.append(node)
        for k in adjlist[node]:
            if color[k] != 1:
                stack.append(k)
                
                
print(*traversal)                
    




