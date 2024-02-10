import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(input())

# print()

# for i in range(N):
#     for j in range(M):
#         print(graph[i][j], end='')
#     print()

count = []
# 8x8 체스판으로 자르기 위해, -7을 해준다
for a in range(N-7):
    for b in range(M-7):
        w_count = 0
        b_count = 0
        # 시작지점
        for i in range(a, a+8):
            for j in range(b, b+8):
                # 짝수라면
                if (i+j) % 2 == 0:
                    # 그리고 W가 아니라 B라면
                    if graph[i][j] != 'W':
                        # W로 칠하는 갯수 + 1
                        w_count += 1
                    # W라면
                    else:
                        # B로 칠하는 갯수 + 1
                        b_count += 1
                # 홀수라면
                else:
                    # 그리고 W가 아니라 B라면
                    if graph[i][j] != 'W':
                        b_count += 1
                    # B라면
                    else:
                        w_count += 1
        count.append(w_count)
        count.append(b_count)

# print(count)
print(min(count))
