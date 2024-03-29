import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        # 상하좌우
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)  #
        # 오른쪽 위
        dfs(x-1, y+1)
        # 왼쪽 위
        dfs(x-1, y-1)
        # 오른쪽 아래
        dfs(x+1, y+1)
        # 왼쪽 아래
        dfs(x+1, y-1)
        return True
    return False


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    island = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                island += 1

    print(island)
