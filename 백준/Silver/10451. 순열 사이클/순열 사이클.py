import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())


def dfs(v):
    visited[v] = True
    nv = graph[v]
    if not visited[nv]:
        dfs(nv)


for _ in range(T):
    N = int(input())

    graph = list(map(int, input().split()))
    # print(graph[1])
    graph.insert(0, 0)
    # print(graph)
    visited = [False] * (N+1)
    count = 0

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            count += 1
    print(count)
