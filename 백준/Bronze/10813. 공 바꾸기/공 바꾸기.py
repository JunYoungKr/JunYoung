N, M = map(int, input().split())

x = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    x[i - 1], x[j - 1] = x[j - 1], x[i - 1]

for i in x:
    print(i, end=' ')


# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 1 4 2 5
