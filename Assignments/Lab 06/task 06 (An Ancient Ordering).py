import sys
from collections import defaultdict
import heapq

n = int(sys.stdin.readline())
words = []
letters = set()
graph = defaultdict(list)
valid = True
in_degree = defaultdict(int)

for _ in range(n):
    a = sys.stdin.readline().strip()
    words.append(a)
    letters.update(a)
    
for i in range(len(words) - 1):
    w1, w2 = words[i], words[i+1]
    minlen = min(len(w1), len(w2))
    diff = False
    
    for j in range(minlen):
        if w1[j] != w2[j]:
            u, v = w1[j], w2[j]
            if v not in graph[u]:
                graph[u].append(v)
                in_degree[v] += 1
            diff = True
            break
    
    if len(w1) > len(w2) and not diff:
        valid = False
        break
        
if valid == False:
    print(-1)
    exit()

def bfs(letters):
    heap = []
    ans = ""
    for char in letters:
        if char not in in_degree:
            in_degree[char] = 0 
    
    for char in sorted(letters):
        if in_degree[char] == 0:
            heapq.heappush(heap, char)
    

    while heap:
        u = heapq.heappop(heap)
        ans = ans + u
        for v in sorted(graph[u]):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)
    if len(ans) != len(letters):
        ans = -1
                
    return ans

res = bfs(letters)

if res != -1:
    print(str(res))
else:                                    
    print(-1)                
            
    
             
    