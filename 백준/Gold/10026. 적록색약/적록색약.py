import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(str, input().rstrip())))

graph1 = copy.deepcopy(graph)
# 적록색약인 사람이 본 구역의 수


def dfs1(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    if graph1[x][y] == 'R' or graph1[x][y] == 'G':
        graph1[x][y] = 0
        # 상하좌우
        dfs1(x-1, y)
        dfs1(x+1, y)
        dfs1(x, y-1)
        dfs1(x, y+1)
        return True
    return False

# 적록색약이 아닌 사람이 본 구역의 수


def dfs2(x, y, color):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    if graph[x][y] == color:
        graph[x][y] = 0
        # 상하좌우
        dfs2(x-1, y, color)
        dfs2(x+1, y, color)
        dfs2(x, y-1, color)
        dfs2(x, y+1, color)
        return True
    return False


# 적록색약인 사람이 봤을 때의 구역의 개수
r_count = g_count = b_count = 0

for i in range(N):
    for j in range(N):
        if dfs2(i, j, 'R') == True:
            r_count += 1
        if dfs2(i, j, 'G') == True:
            g_count += 1
        if dfs2(i, j, 'B') == True:
            b_count += 1

            # 적록색약이 아닌 사람이 봤을 때의 구역의 개수
count = 0
for i in range(N):
    for j in range(N):
        if dfs1(i, j) == True:
            count += 1
print(r_count + g_count + b_count, count + b_count)
