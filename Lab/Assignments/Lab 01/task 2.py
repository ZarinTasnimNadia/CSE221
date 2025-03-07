num = int(input())
for i in range(num):
    calc = input()
    lst = calc.split(" ")
    if lst[2] == "+":
        print(int(lst[1]) + int(lst[3]))
    if lst[2] == "-":
        print(int(lst[1]) - int(lst[3]))
    if lst[2] == "/":
        print(int(lst[1]) / int(lst[3]))
    if lst[2] == "*":
        print(int(lst[1]) * int(lst[3]))            
    test = input().split(" ")
