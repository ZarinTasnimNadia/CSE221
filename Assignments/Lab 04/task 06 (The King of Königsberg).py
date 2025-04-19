import sys
n = int(sys.stdin.readline())


i, j = map(int, sys.stdin.readline().split())




count = 0
pos_moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for m in range(len(pos_moves)):
    pos_moves[m][0] += i
    pos_moves[m][1] += j    
    

    
valid_moves = []
for k in pos_moves:
    if k[0] >= 1 and k[0] <= n and k[1] >= 1 and k[1] <= n:
        count += 1
        valid_moves.append(k)


print(count)
for move in valid_moves:
    print(*move)       
    
    