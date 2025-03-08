import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

close_i = 0
close_j = 0
min_diff = float("inf")
close_sum = 0

i = 0

for j in range(n):
    close_sum += arr[j]
    
    
    while close_sum > k and i <= j:
        
        diff = abs(close_sum - k)
        if diff < min_diff:
            min_diff = diff
            close_i = i 
            close_j = j
            
        close_sum -= arr[i]
        i += 1
    
    diff = abs(close_sum - k)
        
    if diff < min_diff:
        min_diff = diff
        close_i, close_j = i, j 
                  
            
sys.stdout.write(f"{close_i} {close_j}\n") 
