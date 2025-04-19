import sys

n, m = map(int, sys.stdin.readline().split())
matrix = [[0]*n for i in range(n)]

for j in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    matrix[u-1][v-1] = w
    
for k in matrix:
    print(*k)    