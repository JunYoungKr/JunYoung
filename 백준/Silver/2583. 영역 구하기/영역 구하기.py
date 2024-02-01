import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())

graph = [[1] * N for _ in range(M)]
# print(graph)

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0


# for i in range(M):
#     for j in range(N):
#         print(graph[i][j], end=' ')
#     print()
# print()


def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N or graph[x][y] == 0:
        return False
    graph[x][y] = 0
    area = 1
    area += dfs(x-1, y)
    area += dfs(x+1, y)
    area += dfs(x, y-1)
    area += dfs(x, y+1)
    return area


res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            area = dfs(i, j)
            if area > 0:
                res.append(area)

res.sort()  # 영역의 넓이를 오름차순으로 정렬
print(len(res))  # 총 영역의 개수 출력
print(' '.join(map(str, res)))  # 각 영역의 넓이 출력
