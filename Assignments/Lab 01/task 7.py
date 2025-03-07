n = int(input())
name = []
place = []
time = []
train = []

for i in range(n): 
    test1 = input().split()
    train.append((test1[0], test1[4], test1[6]))
    
def name_sort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True

                
                    
        if flag == False:
            break
    return arr    
                
def time_sort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j][0] == arr[j+1][0] and arr[j][2] != arr[j+1][2]:
                t1 = arr[j][2].split(":")
                t2 = arr[j+1][2].split(":")
                if int(t1[0]) < int(t2[0]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = True
                elif int(t1[0]) == int(t2[0]) and int(t1[1]) < int(t2[1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = True
        if flag == False:
            break
        
    return arr

final = time_sort(name_sort(train))
for i in range(n):
    print(f"{final[i][0]} will departure for {final[i][1]} at {final[i][2]}")       
                        
            
             
                    
        
                    