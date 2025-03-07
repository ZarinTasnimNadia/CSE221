n = int(input())
test1 = input().split()
arr = []
brr = []

for i in range(n):
    arr.append(int(test1[i]))
    


while arr:
    if len(arr) == 1:
        brr.append(arr.pop(0))
        break
    left, right = 0, len(arr)-1
    
    if arr[0] > arr[len(arr)-1]:
        brr.append(arr.pop(len(arr)-1))
        
        
    
    if arr[0] <= arr[len(arr)-1]:
        brr.append(arr.pop(0))
         

for j in range(n-1):
    flag = True
    if brr[j] > brr[j+1]:
        flag = False
        print("Impossible")        
        break
if flag == True:
    print("Possible")          
              