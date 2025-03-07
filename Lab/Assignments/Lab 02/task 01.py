N, S = map(int, input().split())
arr = list(map(int, input().split()))

def twoSum(N, S, arr):
    i = 0
    j = N-1
    
    
    while i < j:
        sum = arr[i] + arr[j]
        if sum == S:
            print(i+1, j+1)
            return
            
        elif sum < S:
            i += 1
        elif sum > S:
            j -= 1
        
    print(-1)
                        
twoSum(N, S, arr)            