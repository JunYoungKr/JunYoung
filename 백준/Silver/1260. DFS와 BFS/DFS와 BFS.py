from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)


for i in graph:
    i.sort()


visited = [False] * (N + 1)


def dfs(start):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


dfs(V)

print()

# 주의!! visited 2개를 생성해야함!
visited = [False] * (N + 1)


def bfs(start):
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


bfs(V)
