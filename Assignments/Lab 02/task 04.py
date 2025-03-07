import sys

def binaryString(st, end, num):
    
    while st <= end:
        
        mid = (st + end)//2
    
        if num[mid] == "1" and (num[mid-1] == "0" or mid == 0):
            return mid + 1
        
        elif num[mid] == "0":
            st = mid + 1         
    
        else:
            end = mid - 1
            
    return -1        

N = int(sys.stdin.readline().strip())    
for i in range(N):
    num = str(sys.stdin.readline().strip())
    st, end = 0, len(num) -1
    print(binaryString(st, end, num))  
    