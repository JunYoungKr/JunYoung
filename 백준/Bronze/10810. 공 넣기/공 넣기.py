N, M = map(int, input().split())

x = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j + 1):
        x[n - 1] = k


for i in (x):
    print(i, end=' ')
