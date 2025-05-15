import sys
from collections import deque
from heapq import heappush, heappop

r, h = map(int, sys.stdin.readline().split())
g1 = list(map(int, sys.stdin.readline().split()))
g2 = list(map(int, sys.stdin.readline().split()))
graph = []
for i in range(r):
    row = list(map(str, sys.stdin.readline().strip()))
    graph.append(row)




def bfs(graph, r, h, pos):
    checker = [[False]*h for _ in range(r)]
    dist = [[0]*h for _ in range(r)]
    direction =[[-1, 0], [1, 0], [0, 1], [0, -1]]
    que = deque()
    que.append(pos)
    checker[pos[0]][pos[1]] = True
    
    while que:
        row, col = que.popleft()
        if graph[row][col] == "D": 
            return dist[row][col]    
        
        for i, j in direction:
            new_r, new_col = row + i, col + j
            if -1 < new_r < r and -1 < new_col < h:
                if checker[new_r][new_col] == False and graph[new_r][new_col] != "W":
                    checker[new_r][new_col] = True
                    dist[new_r][new_col] = dist[row][col] + 1
                    que.append([new_r, new_col])
        
    return -1                
        
p1 = bfs(graph, r, h, g1)
p2 = bfs(graph, r, h, g2)

if p1 > p2:
    print("Player 2") 
elif p1 < p2:
    print("Player 1")
else:
    print("Tie")           