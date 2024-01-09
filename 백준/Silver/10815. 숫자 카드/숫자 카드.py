N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

dic = {}

for i in arr2:
    dic[i] = 0


for i in arr:
    if i in dic:
        dic[i] = 1

for i in dic:
    print(dic[i], end=" ")
