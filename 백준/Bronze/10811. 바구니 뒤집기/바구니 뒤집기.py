N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(i+1)


temp = 0
for i in range(M):
    i, j = map(int, input().split())
    temp = arr[i-1:j]
    temp.reverse()
    arr[i-1:j] = temp
    # print(arr)

for i in range(N):
    print(arr[i], end=" ")
