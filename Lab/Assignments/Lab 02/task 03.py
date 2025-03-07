import sys
info1 = sys.stdin.readline()
info2 = sys.stdin.readline()
N, K = map(int, info1.split())
arr = list(map(int, info2.split()))

def MSS(N, K, arr):
    
    length = 0
    sum = 0
    left, right = 0, 0
    
    while right < N:
        sum += arr[right]
        
        while sum > K and left <= right:
            sum -= arr[left]
            left += 1
            
        length = max(length, right + 1 - left )
        right += 1
        
    return length    
            
print(MSS(N,K, arr))            

            
