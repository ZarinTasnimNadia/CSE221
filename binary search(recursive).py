def binarySearch2(key, array, st, end):
    
    
    if st > end:
        return "value does not exist in the array"
    
    mid = (st + end) // 2
    
    if array[mid] == key:
        return mid
    if array[mid] > key:
        return binarySearch2(key, array, st, mid)
    
    return binarySearch2(key, array, mid+1, end)