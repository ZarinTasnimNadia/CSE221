import sys

def tokyo_drift(a, b, mod):
    ans1 = 1
    ans2 = a % mod
    
    while b > 0:
        if b % 2 != 0:
            ans1 = (ans1 * ans2) % mod
            
        ans2 = (ans2*ans2) % mod
        b //= 2  
        
    return ans1      
    
    
        
    # ans = tokyo_drift(a, b//2, mod)
    # ans = (ans*ans) % mod
    # if b % 2 != 0:
    #     ans = (ans*a) % mod
        
    # return ans



def sum_mod(a, n, m):
    
    if n == 1:
        return a % m
    
    sum1 = sum_mod(a, n//2, m)
    power1 = tokyo_drift(a, n//2, m)
    
    mod_sum = (sum1*(1 + power1)) % m
    
    if n % 2 != 0:
        mod_sum = (mod_sum + tokyo_drift(a, n, m)) % m    
        
        
    return mod_sum    
    
    
    
  
           
           
           
test = int(sys.stdin.readline().strip())
for i in range(test):
    a, n, m = map(int, sys.stdin.readline().split())
    ans = sum_mod(a, n, m)
    sys.stdout.write(str(ans) + "\n")
               