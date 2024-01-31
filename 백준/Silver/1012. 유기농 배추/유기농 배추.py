import sys
sys.setrecursionlimit(10000)

# 테스트 케이스 T 입력
T = int(input())


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        # 상하좌우
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False


for i in range(T):
    # 배추밭의 가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K
    M, N, K = map(int, input().split())

    # 배추밭
    graph = [[0] * M for _ in range(N)]

    # K줄에 배추의 위치
    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    res = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                res += 1
    print(res)
