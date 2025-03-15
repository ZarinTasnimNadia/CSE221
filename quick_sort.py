def quickSort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quickSort(arr, low, j - 1)
        quickSort(arr, j + 1, high)
    return arr    


        
def partition(arr, low, high):
    
    pivot = arr[low] 
    i, j = low + 1, high
    
    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1
            
        while j >= low and arr[j] > pivot:
            j -= 1
        
        if i < j:    
            arr[i], arr[j] = arr[j], arr[i]
        
        
    arr[low], arr[j] = arr[j], arr[low]
    return j        
        
 # def medianOfthree(arr, low, high):
    
#     pivot = (low + high)//2
#     if arr[low] <= arr[pivot] <= arr[high]:
#         return
#     if arr[low] < arr[pivot] > arr[high]:
#         arr[low], arr[pivot], arr[]   