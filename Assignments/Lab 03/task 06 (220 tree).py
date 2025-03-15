import sys
n = int(sys.stdin.readline().strip())
in_order = list(map(int, sys.stdin.readline().split()))
pre_order = list(map(int, sys.stdin.readline().split()))

def post_tree(n, in_order, pre_order):
    dict = {}
    for i in range(len(in_order)):
        dict[in_order[i]] = i
        
    def tree_making(pre_st, pre_end, in_st, in_end):
        
        if pre_st > pre_end or in_st > in_end:
            return []
        
        root = pre_order[pre_st]
        root_idx = dict[root] 
        
        left = root_idx - in_st
        
        
        
        left_tree = tree_making((pre_st + 1), (pre_st + left), in_st, (root_idx - 1))
        right_tree = tree_making((pre_st + left + 1), pre_end, (root_idx + 1), in_end)
        
        
        return left_tree + right_tree + [root]
    
    
    return tree_making(0, (len(pre_order) -1), 0, (len(in_order) - 1))   
            
            
ans  = post_tree(n, in_order, pre_order)

print(*ans)            