import sys
n = int(sys.stdin.readline().strip())
test = sys.stdin.readline().strip()
k = int(sys.stdin.readline().strip())
arr = list(map(int, test))

sum = 0
count = 0
left, right = 0, 0
flag = True

while (right - left) != k and left < n and right < n:
    if arr[left] != 0:
        left += 1
    else:
        right += 1    
    
for i in range(left, right, 1):
    if arr[i] == 1:
        count += 1
        flag = False


if flag == False:
    sys.stdout.write(str((count)))
else:
    sys.stdout.write(str((0)))        
        
                
    