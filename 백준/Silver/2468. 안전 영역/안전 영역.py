import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이 계산
max_height = max(max(row) for row in graph)


def dfs(x, y, height):
    if x < 0 or y < 0 or x >= N or y >= N or graph[x][y] < height:
        return False
    graph[x][y] = -1  # 방문한 지점을 -1로 표시하여 방문 처리
    # 주변 탐색 (상하좌우)
    dfs(x-1, y, height)
    dfs(x+1, y, height)
    dfs(x, y-1, height)
    dfs(x, y+1, height)
    return True


result = []
for height in range(1, max_height + 1):
    count = 0
    # 임시 복사본 생성
    temp_graph = [row[:] for row in graph]
    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] >= height:
                if dfs(i, j, height):
                    count += 1
    # 원본 graph 복원
    graph = [row[:] for row in temp_graph]
    result.append(count)

# 최대 안전 영역의 개수 출력
print(max(result))
