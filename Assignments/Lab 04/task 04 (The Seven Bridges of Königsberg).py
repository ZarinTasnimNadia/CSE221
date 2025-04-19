import sys
n, m = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

adj_list = {}
#adj_list = [[]* for _ in range(n)]

for i in range(1, n + 1):
    adj_list[i] = []
    
for k in range(m):
    adj_list[u[k]].append(v[k])
    adj_list[v[k]].append(u[k])
        

    
    
    
odd_count = 0    
for j in adj_list.keys():
    if len(adj_list[j]) % 2 != 0:
        odd_count += 1
        
if odd_count > 2:
    print("NO")
else:
    print("YES")            
          
