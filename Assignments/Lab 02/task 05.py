import sys
test1 = sys.stdin.readline().strip()
test2 = sys.stdin.readline().strip()
n, q = map(int, test1.split())
arr = list(map(int, test2.split()))


def getLower(r1, arr):
    
    lower, upper = 0, len(arr)
    
    while lower < upper:
        
        mid = (lower + upper)//2
        if arr[mid] >= r1:
            upper = mid
        else:
            lower = mid + 1 
            
    return lower


def getUpper(r2, arr):
    
    lower, upper = 0, len(arr)
    
    while lower < upper:
                      
        mid = (lower + upper)// 2
        if arr[mid] > r2:
            upper = mid
        else:
            lower = mid + 1
            
    return lower
    

def countNumber(r1, r2, arr):
    
    low, high = getLower(r1, arr), getUpper(r2, arr)
    
    
    count = high - low    
    
            
    return count        
             


for i in range(q):
    test = sys.stdin.readline().strip()
    r1, r2 = map(int, test. split())   
    result = countNumber(r1, r2, arr)
    sys.stdout.write(str(result)+ "\n") 
