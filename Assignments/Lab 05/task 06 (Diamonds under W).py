import sys
from collections import deque
r, h = map(int, sys.stdin.readline().split())
matrix = []

for j in range(r):
    row = list(sys.stdin.readline().strip())
    matrix.append(row)

    
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
checker = [[False] * h for _ in range(r)]

def bfs(st_row, st_col):
    q = deque()
    q.append((st_row, st_col))
    
    checker[st_row][st_col] = True
    diamonds = 0

    while q:
        row, col = q.popleft()
        if matrix[row][col] == "D":
            diamonds += 1

        for i, j in direction:
            new_r, new_c = row + i, col + j
            
            
            if 0 <= new_r and new_r < r and 0 <= new_c and new_c < h: 
                if checker[new_r][new_c] == False and matrix[new_r][new_c] != '#':
                    checker[new_r][new_c] = True
                    q.append((new_r, new_c))
                
    return diamonds

max_diamonds = 0
for i in range(r):
    
    for j in range(h):
    
        if matrix[i][j] != "#" and checker[i][j] != True:
            diamonds = bfs(i, j)
            max_diamonds = max(max_diamonds, diamonds)

print(max_diamonds)
                            
                
                
                 
                       
        
        
    
    
    
        