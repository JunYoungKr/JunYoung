import sys
from collections import deque
input = sys.stdin.readline

# 테스트케이스 T
T = int(input())


def bfs():
    queue = deque()
    queue.append([home[0], home[1]])
    while queue:
        x, y = queue.popleft()
        # 상근이와 친구들이 행복하게 페스티벌에 갈 수 있는 경우
        if abs(x-fest[0]) + abs(y-fest[1]) <= 1000:
            print("happy")
            return
        # 중간에 맥주가 바닥나서 더 이동할 수 없는 경우
        for i in range(n):
            if not visited[i]:
                nx, ny = conv[i]
                # print("nx, ny:", nx, ny)
                if abs(x-nx) + abs(y-ny) <= 1000:
                    queue.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return


for _ in range(T):
    # 편의점의 개수
    n = int(input())
    home = list(map(int, input().split()))

    # 편의점 n개만큼 입력
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    # print(conv)

    # 페스티벌 장소 좌표 입력
    fest = list(map(int, input().split()))
    visited = [0 for _ in range(n+1)]
    bfs()
