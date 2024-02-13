import sys
from collections import deque
input = sys.stdin.readline

# 수빈이는 점 N, 동생은 점 K
# 수빈이의 현재 위치가 X일때
# 걷는다면 1초후에는 X-1 or X+1
# 순간이동은 2*X

N, K = map(int, input().split())

visited = [0 for _ in range(100001)]


def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        # 수빈이와 동생을 찾은 경우
        if v == K:
            return visited[v]
        # 이동을 하는 경우
        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)


print(bfs(N))
