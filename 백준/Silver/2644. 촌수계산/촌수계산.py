import sys
from collections import deque
input = sys.stdin.readline

# 전체 사람의 수
N = int(input())

# 촌수를 계산해야하는 서로 다른 두 사람의 번호
p1, p2 = map(int, input().split())

# 부모 자식들 간의 관계의 계수 m
m = int(input())

graph = [[] for _ in range(N+1)]
for i in range(m):
    # 부모 자식간의 관계를 나타내는 x, y
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)
# print(graph)


def bfs(start, end):
    queue = deque([start])
    visited[False] * len(graph)
    distance = [0] * len(graph)
    visited[start] = True
    # print(queue)
    # visited[v] = True
    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        if v == end:
            return distance[end]
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[v] + 1
                # print("distance", distance)
                queue.append(i)
    return -1


distance = bfs(p1, p2)
print(distance)


def bfs(start, end):
    queue = deque([start])
    visited[start] = True
