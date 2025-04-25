import sys 
n,m = map(int, sys.stdin.readline().split())
mydict = {i : [] for i in range(1, n+1)}
for j in range(m):
    u, v = map(int, sys.stdin.readline().split())
    mydict[u].append(v)  
    mydict[v].append(u)

for neighbours in mydict.values():
    neighbours.sort()
    
q = []
color = [0] * (n+1)
traversal = []

q.append(1)
color[1] = 1

while q != []:
    node = q.pop(0)
    traversal.append(node)
    for value in mydict[node]:
        if color[value] != 1:
            color[value] = 1
            q.append(value)
            
            
print(*traversal)            
    
    


    
    
        
      