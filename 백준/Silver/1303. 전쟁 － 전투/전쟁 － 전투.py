import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(N)]

# print()
# print(graph)

W_ = []
B_ = []

count = 0


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if graph[x][y] == 'W':
        graph[x][y] = 0
        global count
        count += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(N):
    for j in range(M):
        if dfs(i, j):
            dfs(i, j)
            W_.append(count)
            count = 0

# print(W_)

count1 = 0


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if graph[x][y] == 'B':
        graph[x][y] = 0
        global count1
        count1 += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(N):
    for j in range(M):
        if dfs(i, j):
            dfs(i, j)
            B_.append(count1)
            count1 = 0

# print(B_)

W_total = 0
for i in W_:
    W_total += i ** 2

B_total = 0
for i in B_:
    B_total += i ** 2

print(W_total, B_total)
