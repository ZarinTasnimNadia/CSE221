def binarySearch(key, array, st, end):
    
    while st <= end:
        mid = (st + end) // 2
        
        if array[mid] == key:
            return mid
        if array[mid] > key:
            end = mid - 1
        if array[mid] < key:
            st = mid + 1    

    return "value does not exist in the array"