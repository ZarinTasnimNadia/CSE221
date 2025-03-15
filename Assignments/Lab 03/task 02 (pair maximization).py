import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))


def find_max_pair(arr, left, right):
    
    if right - left < 1 :
        return float("-inf")
    if right - left == 1:
        return arr[left] + arr[right]**2
    
    

    mid = (left + right)//2
    
    left_arr = find_max_pair(arr, left, mid)
    right_arr = find_max_pair(arr, mid+1, right)
    
    
    find_max = max(arr[left:mid+1])
    
    find_pair = float("-inf")
    for j in range(mid + 1, right + 1):
        find_pair = max(find_pair, find_max + arr[j]**2)
    

    
    return max(find_pair, left_arr, right_arr)
    
    
    
ans = find_max_pair(arr, 0, n-1)    
sys.stdout.write(str(ans))        
    















# import sys

# n = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().split()))


# def find_max(arr, i, j):
    
#     if i == j:
#         return i
#     mid = (i + j)//2
    
#     left_max = find_max(arr, i, mid)
#     right_max = find_max(arr, mid+1, j)
    
#     if abs(arr[left_max]) > abs(arr[right_max]):
#         #print("left", left_max, arr[left_max])
#         return left_max
#     else:
#        #print("right", right_max, arr[right_max])
#         return right_max
    
# j = find_max(arr, 0, len(arr) - 1)
# #print("j", j)
# i = find_max(arr, 0, j-1)
# #print("i", i)
# ans = arr[i] + arr[j]**2
# sys.stdout.write(str(ans))    
     
    
    




# def partition(arr):
    
#     n = len(arr)
#     if n <= 1:
#         return arr
#     mid = n//2
#     left = arr[:mid]
#     right = arr[mid+1:]
    
#     left = partition(left)
#     right = partition(right)
#     ans = find_max(left, right)
#     return ans


# def find_max(arr1, arr2):
#     max1, max2 = 0, 0
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j] and max1 < arr2[j]:
    
#             max1 = arr2[j]
#             j += 1
            
#         if arr1[i] > arr2[j] and max1 < arr2[i]:
#             max1 = arr2[i]
#             i += 1
            
#         i += 1
#         j += 1
        
                 
            
        
    
     
    
    
        






































# import sys

# n = int(sys.stdin.readline().strip())
# array = list(map(int, sys.stdin.readline().split()))



# def pairMax(arr):
    
#     arr = list(map(abs, arr))
#     sorted = mergeSort(arr)
    
#     max = abs((sorted[len(arr) - 1]*sorted[len(arr) - 1])) + sorted[len(arr) - 2]
    
#     return max
 
# def mergeSort(array):
    
#     n = len(array)
    
#     if n <= 1:
#         return array
    
#     mid = n//2
#     left = array[0: mid]
#     right = array[mid: ]
    
#     left = mergeSort(left)
#     right = mergeSort(right)
#     ans = merge(left, right)
#     return ans    
        
 
# def merge(arr1, arr2):
#     i, j = 0, 0
#     merged = []
    
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             merged.append(arr1[i])
#             i += 1
            
#         else:
#             merged.append(arr2[j]) 
#             j += 1
            
#     while i < len(arr1):
#         merged.append(arr1[i])
#         i += 1
        
#     while j < len(arr2):
#         merged.append(arr2[j])
#         j += 1
        
#     return merged    
    

# print(pairMax(array))    