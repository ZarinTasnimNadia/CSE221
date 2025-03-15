import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

def inv_count(arr, i, j):
    inv = 0
    
    
    if i < j:
    
        mid = (i+j)//2
        inv += inv_count(arr, i, mid)
        inv += inv_count(arr, mid+1, j)
        inv += merge(arr, i, mid, j)
        
    return inv

def merge(arr, left, mid, right):
    inv = 0
    l_arr = arr[left:mid+1]
    r_arr = arr[mid+1: right+1]
    # i = left
    # j = mid+1
    i = j = 0
    k = left
    merged = []
    
    # while i <= mid and j <= right:
    while i < len(l_arr) and j < len(r_arr):
        
        if l_arr[i] <= r_arr[j]:
            #merged.append(arr[i])
            arr[k] = l_arr[i]
            i += 1
        else:
            #merged.append(arr[j])
            arr[k] = r_arr[j]
            inv += len(l_arr) - i
            j += 1
        k += 1
            
    while i < len(l_arr):
        #merged.append(arr[i])
        arr[k] = l_arr[i]
        i += 1
        k += 1
        
    while j < len(r_arr):
        #merged.append(arr[j])
        arr[k] = r_arr[j]
        j += 1
        k += 1
    
    return inv

    
inv = inv_count(arr, 0, len(arr) -  1)
                    
print(inv)            
print(*arr)   
            
            
    










































# import sys

# n = int(sys.stdin.readline().strip())
# array = list(map(int, sys.stdin.readline().split()))

# def merge(arr1, arr2):
#     i = j = 0
#     merged = []
#     inversion = 0
    
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             merged.append(arr1[i])
#             i += 1
            
#         else:
#             merged.append(arr2[j])
#             inversion += len(arr1) - i
#             j += 1
                
        
#     while i < len(arr1):
#         merged.append(arr1[i])
#         i += 1
        
#     while j < len(arr2):
#         merged.append(arr2[j])
#         j += 1
        
#     return merged, inversion

# def mergeSort(arr):
#     n = len(arr)
    
#     if n <= 1:
#         return arr, 0
    
#     mid = n//2
        
#     left = arr[:mid]
#     right = arr[mid:]
    
#     left, l_inv = mergeSort(left)
#     right, r_inv = mergeSort(right)
#     ans, inv = merge(left, right)
#     total_inv = l_inv + r_inv + inv
#     return ans, total_inv
                     
# array, inv = mergeSort(array)                    

# print(inv)
# print(*array)