import sys

n, m = map(int, sys.stdin.readline().split())
adjlist = [[] for x in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adjlist[u].append(v)
    
    
    