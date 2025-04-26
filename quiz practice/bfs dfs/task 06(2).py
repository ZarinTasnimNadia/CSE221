import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

matrix = []
checker = [[False]*m for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(n):
    row = list(sys.stdin.readline().strip())
    matrix.append(row)

def bfs(i, j):
    que = deque()
    que.append((i, j))
    checker[i][j] = True
    diamonds = 0
    
    while que:
        row, col = que.popleft()
        if matrix[row][col] == "D":
            diamonds += 1
            
        for a, b in direction:
            new_r = row + a
            new_c = col + b
            
            if 0 <= new_r and new_r < n and 0 <= new_c and new_c < m:
                if matrix[new_r][new_c] != "#" and checker[new_r][new_c] == False:
                    checker[new_r][new_c] = True
                    que.append((new_r, new_c))
    return diamonds
    
max_diamonds = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] != "#" and checker[i][j] == False:
            diamonds = bfs(i, j)
            
            max_diamonds = max(max_diamonds, diamonds)
        
print(max_diamonds)                                        