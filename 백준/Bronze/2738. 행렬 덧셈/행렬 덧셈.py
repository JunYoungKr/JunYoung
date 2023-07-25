N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr1 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr[i][j] += arr1[i][j]
        print(arr[i][j], end=' ')
    print()
