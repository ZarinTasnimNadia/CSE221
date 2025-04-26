import sys
from collections import deque

r, h = map(int, sys.stdin.readline().split())

matrix = []

for i in range(h):
    row = list(sys.stdin.readline().strip())
    matrix.append(row)
checker = [[False]*h for _ in range(r)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
def bfs(row, col):
    que = deque()
    que.append((row, col))
    checker[row][col] = True
    diamonds = 0
    
    while que:
        row1, col1 = que.popleft()
        if matrix[row1][col1] == "D":
            diamonds += 1
        
        for i, j in direction:
            new_r, new_c = row1 + i, col1 + j
            
            if 0 <= new_r and new_r < r and new_c < h and 0 <= new_c:
                if matrix[new_r][new_c] != "#" and checker[new_r][new_c] == False:
                    checker[new_r][new_c] = True
                    que.append((new_r, new_c))     
                    
    return diamonds


max_diamonds = 0

for i in range(r):
    for j in range(h):
        if matrix[i][j] != "#" and checker[i][j] == False:
            diamonds = bfs(i, j)       
            max_diamonds = max(max_diamonds, diamonds)         
            
print(max_diamonds)    
    
    
