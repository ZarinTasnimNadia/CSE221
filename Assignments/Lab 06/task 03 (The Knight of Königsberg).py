import sys
from collections import deque

n = int(sys.stdin.readline())
#board = [[] for x in range(n+1)]
checker = [[False]*(n+1) for y in range(n+1)]

a, b, x, y = map(int, sys.stdin.readline().split())
checker[a][b] = True

directions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                  (2, 1), (1, 2), (-1, 2), (-2, 1)]
que = deque()
que.append((a, b))

count = 0

while que:
    length = len(que)
    for _ in range(length):
        x1, y1 = que.popleft()
        
        
        for i, j in directions:
            x2, y2 = x1 + i, y1 + j
            
            if (1 <= x2 <= n) and (1 <= y2 <= n) and not checker[x2][y2]: 
                if (x2, y2) == (x, y):
                    count += 1
                    print(count)  
                    exit()
                
                checker[x2][y2] = True
                que.append((x2, y2))
    count += 1
            
print(-1)         
                