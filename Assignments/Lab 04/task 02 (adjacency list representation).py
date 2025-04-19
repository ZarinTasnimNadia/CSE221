import sys
n, m = map(int, sys.stdin.readline().split())

adj_list = [[] for x in range(n + 1)]

u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    adj_list[u[i]].append((v[i], w[i]))
    
for j in range(1, len(adj_list)):
    print(f"{j}: ", end = "")
    print(*adj_list[j])
          
    
            
        
            