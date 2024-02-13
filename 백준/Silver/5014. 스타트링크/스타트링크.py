import sys
from collections import deque
input = sys.stdin.readline

# 건물은 총 F층
# 강호는 S층에서 G층으로 이동하려고 함
# U버튼은 위로 D버튼은 아래로 가는 버튼
# 엘리베이터를 이용하여 G층에 갈 수 없다면, "use the stairs" 출력

# F S G U D 입력
F, S, G, U, D = map(int, input().split())

# 10 1 10 2 1
# 10층짜리 건물인데 현재 1층, 10층으로 이동하려고 한다. Up은 2층씩, Down은 1층씩
# 눌러야 하는 버튼의 수의 최솟값을 출력
# bfs 사용

visited = [0 for _ in range(F+1)]


def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == G:
            return visited[v]
        for i in (v+U, v-D):
            if 0 < i <= F and not visited[i] and i != start:
                visited[i] = visited[v] + 1
                queue.append(i)
    return "use the stairs"


print(bfs(S))
