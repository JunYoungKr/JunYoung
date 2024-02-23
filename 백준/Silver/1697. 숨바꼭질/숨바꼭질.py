from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N, K = map(int, input().split())

visited = [0 for _ in range(100001)]


def bfs(start, end):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v == K:
            return visited[v]
        for i in (v+1, v-1, v*2):
            # print(i)
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)


print(bfs(N, K))
