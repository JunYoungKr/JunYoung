N, M = map(int, input().split())

arr = []

arr = list(map(int, input().split()))

a = 0
res = []
sum = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if (arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k]):
                sum = arr[i] + arr[j] + arr[k]
                if sum <= M:
                    res.append(sum)

res = set(res)

print(max(res))
