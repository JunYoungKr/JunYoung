from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 세로크기 n, 가로크기 m
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]


# def dfs(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         global count
#         count += 1
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True
#     return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    graph[x][y] = 0
    queue = deque()
    queue.append([x, y])
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = 0
                count += 1
    return count


ans = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            ans = max(bfs(i, j), ans)

print(cnt, ans)
