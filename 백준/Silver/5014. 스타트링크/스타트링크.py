from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


F, S, G, U, D = map(int, input().split())

visited = [0 for _ in range(F+1)]


def bfs(start):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v == G:
            return visited[v]
        for i in (v + U, v - D):
            # print(i)
            if 0 < i <= F and not visited[i] and i != start:
                visited[i] = visited[v] + 1
                queue.append(i)
    return 'use the stairs'


print(bfs(S))
