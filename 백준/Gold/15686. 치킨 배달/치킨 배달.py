import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]


home = []
chicken = []

for i in range(N):
    for j in range(N):
        # 집인 경우
        if map[i][j] == 1:
            home.append([i, j])
        elif map[i][j] == 2:
            chicken.append([i, j])

# print(home)
# print(chicken)

res = 999999
for chi in combinations(chicken, M):  # M개의 치킨집 선택
    # 도시의 치킨 거리
    dist_chick = 0
    for i in home:
        chi_len = 999  # min값을 구하기 위해 값을 크게 설정
        # M만큼 돌면서 가장 가까운 치킨 거리를 구함
        for j in range(M):
            chi_len = min(chi_len, abs(i[0]-chi[j][0]) + abs(i[1]-chi[j][1]))
            # print(chi_len)
        dist_chick += chi_len
    res = min(res, dist_chick)

print(res)
