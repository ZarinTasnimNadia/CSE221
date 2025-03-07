n = int(input())
id = []
mark = []
test1 = input().split()
test2 = input().split()
swap = 0

for i in range(n):
    id.append(int(test1[i]))
    mark.append(int(test2[i]))
    
for j in range(n):
    max_mark = j
    for k in range(j+1, n):
    
        if mark[max_mark] < mark[k]: 
            max_mark = k
            
        elif mark[max_mark] == mark[k] and id[max_mark] > id[k]:
            max_mark = k
            
    if max_mark != j:
        mark[j], mark[max_mark] = mark[max_mark], mark[j]
        id[j], id[max_mark] = id[max_mark], id[j]
        swap += 1        

print(f"Minimum swaps: {swap}")        
for m in range(n):
    print(f"ID: {id[m]} Mark: {mark[m]}")
                           
    