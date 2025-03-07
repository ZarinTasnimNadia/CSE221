num = input().split(" ")
n = int(num[0])
k = int((num[1]))

test = input().split(" ")
array = []

for i in range(n):
     array.append(int(test[i]))

for j in range(n//2):
    value = array[n-1-j]
    array[n-1-j] = array[j]
    array[j] = value

for m in array[n-k:]:
    print(m, end = " ")       