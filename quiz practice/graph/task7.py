import sys
n, q = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
length = n+1

for m in range(1, length):
    for k in range(1, length):
        if m != k:
            x, y = m, k
            while y != 0:
                x, y = y, (x % y)
            if x == 1:
                graph[m].append(k)
                
                
for j in range(q):
    a, b = map(int, sys.stdin.readline().split())
    if b <= len(graph[a]):
        print(graph[a][b-1])
    else:
        print(-1)                         
                
            
