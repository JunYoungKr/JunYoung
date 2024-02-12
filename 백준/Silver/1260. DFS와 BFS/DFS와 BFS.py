import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
for i in graph:
    i.sort()
visited = [False] * (N+1)


def dfs(V):
    visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(i)


dfs(V)

print()
visited2 = [False] * (N+1)


def bfs(V):
    queue = deque([V])
    visited2[V] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited2[i]:
                visited2[i] = True
                queue.append(i)


bfs(V)
