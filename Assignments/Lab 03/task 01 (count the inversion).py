import sys

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))

def merge(arr1, arr2):
    i = j = 0
    merged = []
    inversion = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
            
        else:
            merged.append(arr2[j])
            inversion += len(arr1) - i
            j += 1
                
        
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged, inversion

def mergeSort(arr):
    n = len(arr)
    
    if n <= 1:
        return arr, 0
    
    mid = n//2
        
    left = arr[:mid]
    right = arr[mid:]
    
    left, l_inv = mergeSort(left)
    right, r_inv = mergeSort(right)
    ans, inv = merge(left, right)
    total_inv = l_inv + r_inv + inv
    return ans, total_inv
                     
array, inv = mergeSort(array)                    

print(inv)
print(*array)