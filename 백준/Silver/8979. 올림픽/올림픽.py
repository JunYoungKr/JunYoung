import sys
input = sys.stdin.readline

# 국가의 수 N, 등수를 알고 싶은 국가 K
N, K = map(int, input().split())

medal = []
for _ in range(N):
    medal.append(list(map(int, input().split())))

# print(medal)

medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
# print(medal)

for i in range(N):
    # 찾으려는 국가가 일치하는 경우
    if medal[i][0] == K:
        index = i
# print(index)

for i in range(N):
    # 모든 메달의 수가 같은 경우
    if medal[index][1:] == medal[i][1:]:
        print(i+1)
        break
