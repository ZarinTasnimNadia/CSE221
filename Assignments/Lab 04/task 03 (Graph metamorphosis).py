import sys
n = int(sys.stdin.readline())
matrix = [[0]*n for m in range(n)]

for i in range(n):
    edge = list(map(int, sys.stdin.readline().split()))
    if len(edge) > 1:
        for j in range(1, len(edge)):
            matrix[i][edge[j]] = 1
            
            
for k in matrix:
    print(*k)            
            