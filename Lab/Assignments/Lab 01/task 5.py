n = int(input())
array = input().split()
arr = []

for i in range(n):
    arr.append(int(array[i]))   




def bubbleSort(arr):      
    
                                                   
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
    
        if flag == False:
            break             
        
    
bubbleSort(arr)  
for k in arr:
    print(k, end = " ")  