import sys
a, b = map(int, sys.stdin.readline().split())
mod = 107

def tokyo_drift(a, b, mod):
    if b == 0:
        return 1
    
        
    ans = tokyo_drift(a, b//2, mod)
    ans = (ans*ans) % mod
    if b % 2 != 0:
        ans = (ans*a) % mod
        
    return ans
    
             
             
ans = tokyo_drift(a, b, mod)
sys.stdout.write(str(ans))             