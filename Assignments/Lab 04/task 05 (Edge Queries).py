import sys
n, m =  map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

adj_list = {i : [] for i in range(1, n+1)}
diff_count = [0] * n

for j in range(m):
    adj_list[u[j]].append(v[j])
    diff_count[u[j] - 1] -= 1
    diff_count[v[j] - 1] += 1
    
print(* diff_count)