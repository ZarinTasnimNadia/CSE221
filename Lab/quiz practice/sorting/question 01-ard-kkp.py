


n = int(input())
test1 = input().split()
arr = []

for i in range(n):
    arr.append(int(test1[i]))
    
swap = 0

for j in range(n):
    min_idx = j
    for k in range(j+1, n):
        if arr[k] < arr[min_idx]:
            min_idx = k
            
    if min_idx != j:
        arr[j], arr[min_idx] = arr[min_idx], arr[j]
        swap += 1

print(arr)        
print(swap)                    
                