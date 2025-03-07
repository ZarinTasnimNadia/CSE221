n,k = input().split()
n = int(n)
k = int(k)
test1 = input().split()
array = []
swap = 0

for i in range(n):
    array.append(int(test1[i]))
    
for j in range(n):
    max_idx = j
    
    for m in range(j+1, n):
        if array[max_idx] < array[m]:
            max_idx = m
    
    if max_idx != j:
        array[max_idx], array[j] = array[j], array[max_idx]
        swap += 1            
        
if swap > k:
    print("Impossible")
else:
    print("Possible")            