n = int(input())
test1 = input().split()
arr = []
even_arr = []
odd_arr = []

for m in range(n):
    arr.append(int(test1[m]))
    
def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = True
                
        if flag == False:
            break
    return arr

for even in arr[0:n:2]:
    even_arr.append(even)
even_arr = bubble_sort(even_arr)
for odd in arr[1:n:2]:
    odd_arr.append(odd)
odd_arr = bubble_sort(odd_arr)
print(even_arr, odd_arr)
even_pointer, odd_pointer = 0,0

for i in range(n):
    if i % 2 == 0:
        arr[i] = even_arr[even_pointer]
        even_pointer += 1  
        
    else:
        arr[i] = odd_arr[odd_pointer]
        odd_pointer +=1
        
print(arr)
flag = True
for j in range(len(arr) - 1):  
    if arr[j] > arr[j+1]:
        flag = False
        print("Impossible")
        break          
if flag == True:
    print("Possible")    
        
                        
        
                    
             