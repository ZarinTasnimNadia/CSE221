import sys
n, q = map(int, sys.stdin.readline().split())

adj_list = [[] for i in range(n)]

for m in range(n):
    for k in range(n):
        if m != k:
            x, y = m + 1, k + 1
            while y != 0:
                x, y = y, (x % y)
            if x == 1:
                adj_list[m].append(k + 1)
            
            
for j in range(q):
    a, b = map(int, sys.stdin.readline().split())
    if b <= len(adj_list[a-1]):
        print(adj_list[a-1][b-1])
    else:
        print(-1)
            
                    