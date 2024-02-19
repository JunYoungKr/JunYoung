import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for _ in range(T):

    # 가로길이 M, 세로길이 N, 심어져있는 위치의 개수 K
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    # print(graph)

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    # print(graph)

    res = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                res += 1
    print(res)
