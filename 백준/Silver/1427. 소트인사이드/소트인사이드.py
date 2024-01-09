N = int(input())

arr = []

while N > 0:
    arr.append(N % 10)
    N //= 10

arr.sort()
arr.reverse()

for i in range(len(arr)):
    print(arr[i], end="")
