from collections import deque
import sys
input = sys.stdin.readline

# 컴퓨터의 수
N = int(input())

# 쌍의 수
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)

visited = [False] * (N+1)

# res = 0


# def bfs(v, graph):
#     visited[v] = True
#     queue = deque([v])
#     res = 0
#     while queue:
#         v = queue.popleft()
#         # res += 1
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#                 res += 1
#     print(res)


# bfs(1, graph)

res = 0


def dfs(v, graph):
    visited[v] = True
    global res
    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph)
            res += 1
    return res


print(dfs(1, graph))
