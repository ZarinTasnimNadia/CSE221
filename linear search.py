def linearSearch(key, array):
    i = 0
    while i < len(array):
        if array[i] == key:
            return i
        i += 1
        
    return "value does not exist in the array"  