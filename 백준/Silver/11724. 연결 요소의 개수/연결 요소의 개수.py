import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 정점의 개수 N, 간선의 개수 M
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 그래프 작성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
visited = [False] * (N + 1)

# dfs 기본 코드


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 연결된 노드의 수
count = 0

# dfs가 끝날 때마다
for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1
print(count)
