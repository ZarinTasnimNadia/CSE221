import sys
from collections import deque
from heapq import heappop, heappush

row, col, color = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
info = [row, col, color]
graph = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

def bfs(graph ,n ,m ,info):    
    checker = [[False]*m for _ in range(n)]
    direction = [[-1, -1], [1, -1], [1, 1], [-1, 1]]
    que = deque()
    que.append(info)
    
    while que:
        row, col, color = que.popleft()
        checker[row][col] = True
        if graph[row][col] == 1:
            graph[row][col] = color
            
        for i, j in direction:
            new_r, new_c = row+i, col+j
            if -1 < new_r < n and -1 < new_c < m:
                if checker[new_r][new_c] == False and graph[new_r][new_c] != 0:
                    que.append([new_r, new_c, color])
    return graph
print("-----------------------------------------------------------------------")
ans = bfs(graph, n, m, info)
for j in ans:
    print(*j)                  
            
    
    