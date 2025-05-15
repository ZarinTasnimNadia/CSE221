import sys
from collections import deque
from heapq import heappop, heappush

n, m, k = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    
def bfs(graph, n, m, k):
    n = len(graph)
    color = ["white"]*n
    parent = [[None]*m for _ in range(n)]
    que = deque()
    que.append((0, 0))
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    checker = [[False]*m for _ in range(n)]
    path = []
    found = [False]
    
    while que:
        row, col = que.popleft()
        if row == n-1 and col == m-1:
            found[0] = True
            break
        
        diff = 0
        checker[row][col] = True
        for r, c in direction:
            new_r, new_c = row+r, col+c
            if 0 <= new_r < n and 0 <= new_c < m:
                diff = abs(graph[row][col] - graph[new_r][new_c])
                if checker[new_r][new_c] == False and diff <= k:
                    que.append((new_r, new_c))
                    parent[new_r][new_c] = (row, col)
    if found[0] == False:
        return [0]
    row, col = n-1, m-1
    while (row, col) != (0, 0):
        path.append((row+1, col+1))
        row, col = parent[row][col]
    path.append((1, 1))
    path.reverse()
    return path    

ans = bfs(graph, n, m, k)
print(*ans)
    