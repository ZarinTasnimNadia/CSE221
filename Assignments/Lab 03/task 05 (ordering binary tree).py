import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

def order_binarytree(n, arr):
    
    def mid_handle(st, end):
        
        if st > end:
            return []
        mid = (st + end) // 2
        
        return ([arr[mid]] + mid_handle(st, mid-1) + mid_handle(mid+1, end))

    return mid_handle(0, n - 1)


ans = order_binarytree(n, arr)

print(*ans)