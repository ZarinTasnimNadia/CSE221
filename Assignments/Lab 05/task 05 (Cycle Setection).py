import sys
n, m = map(int, sys.stdin.readline().split())

adjlist = [[] for i in range(n+1)]
for j in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adjlist[u].append(v)



def colorr(adjlist, n):
    color = [0] * (n+1)
    flag = [False]
    for u in range(1, len(color)):
        if color[u] == 0:
            dfs(adjlist, color, u, flag) 
    if flag[0] == True:
        print("YES")
    else:
        print("NO")            
               

def dfs(adjlist, color, u, flag):
    
    color[u] = 1
    for v in adjlist[u]:
        if color[v] == 0:
            dfs(adjlist, color, v, flag)
        elif color[v] == 1:
            flag[0] = True
            break   
            
            
    color[u] = 2 
    return flag
    
colorr(adjlist, n) 
    
    