N = int(input())

arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((y, x))

arr.sort()

# print(arr)
# print()

for i in range(N):
    print(arr[i][1], arr[i][0])
