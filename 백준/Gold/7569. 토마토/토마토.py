import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

queue = deque()
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False]*M for _ in range(N)] for _ in range(H)]


# print()
# print(graph)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= H or ny >= N or nz >= M:
                continue
            # 익지 않은 토마토가 0, 익은 토마토가 1이기 때문에
            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = True


# 1이 아닌 경우
for a in range(H):
    for b in range(N):
        for c in range(M):
            if graph[a][b][c] == 1 and visited[a][b][c] == 0:
                queue.append((a, b, c))
                visited[a][b][c] = True

bfs()

ans = 0
for a in graph:
    for b in a:
        for c in b:
            # 안익은 토마토가 하나라도 있을 경우
            if c == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(b))

print(ans-1)
