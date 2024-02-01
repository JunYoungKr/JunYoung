import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# for i in range(2, len(graph)):
    # print(graph[i][0])

visited = [False] * (N + 1)

arr = [0] * (N + 1)


def dfs(v):
    visited[v] = True
    # print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            arr[i] = v
            dfs(i)


dfs(1)

for i in range(2, len(arr)):
    print(arr[i])
