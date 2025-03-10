import sys

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))



def pairMax(arr):
    
    arr = list(map(abs, arr))
    sorted = mergeSort(arr)
    
    max = abs((sorted[len(arr) - 1]*sorted[len(arr) - 1])) + sorted[len(arr) - 2]
    
    return max
 
def mergeSort(array):
    
    n = len(array)
    
    if n <= 1:
        return array
    
    mid = n//2
    left = array[0: mid]
    right = array[mid: ]
    
    left = mergeSort(left)
    right = mergeSort(right)
    ans = merge(left, right)
    return ans    
        
 
def merge(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
            
        else:
            merged.append(arr2[j]) 
            j += 1
            
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged    
    

print(pairMax(array))    