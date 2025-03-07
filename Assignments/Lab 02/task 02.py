import sys
N = int(sys.stdin.readline().strip())
alice_arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
bob_arr = list(map(int, sys.stdin.readline().split()))



def mergeArray(N, M, alice_arr, bob_arr):
    new_arr = []
    alice, bob = 0, 0
    while alice < N and bob < M:
        if alice_arr[alice] < bob_arr[bob]:
            
            new_arr.append(alice_arr[alice])
            alice += 1        
        else: 
            
            new_arr.append(bob_arr[bob])
            bob += 1
            
    if bob < M:
        new_arr.extend(bob_arr[bob:])
        
        
        
    if alice < N:
        new_arr.extend(alice_arr[alice:])
        
       
    return new_arr   

merged_arr = mergeArray(N, M, alice_arr, bob_arr)
sys.stdout.write(" ".join(map(str, merged_arr)))
            