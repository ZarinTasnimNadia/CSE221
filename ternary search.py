def ternarySearch(key, array, st, end):
    
    if st > end:
        return "value does not exist in the array"
    
    mid1 = st + ((end - st)//3)
    mid2 = end - ((end - st)//3)
    
    if array[mid1] == key:
        return mid1
    elif array[mid2] == key:
        return mid2
    
    elif array[mid1] > key:
        return ternarySearch(key, array, st, mid1 - 1)
    elif array[mid2] < key:
        return ternarySearch(key, array, mid2 + 1, end)
    else:
        return ternarySearch(key, array, mid1 + 1, mid2 - 1)    