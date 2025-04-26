import sys
n = int(sys.stdin.readline())
#graph = [[] for _ in range(n+1)]
length = n+1
count = 0
a, b = map(int, sys.stdin.readline().split())

pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for k in range(len(pos)):
    pos[k][0] += a
    pos[k][1] += b
    
valid = []

for m in pos:
    if m[0] >= 1 and m[0] <= n and m[1] <= n and m[1] >= 1:
        count += 1
        valid.append(m)
      
     
           
print(count)
for i in valid:
    print(*i)



