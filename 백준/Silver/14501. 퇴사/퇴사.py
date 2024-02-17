import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())

T = [0] * N
P = [0] * N

dp = [0] * (N+1)

for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N-1, -1, -1):
    # 상담완료가 가능할 때
    if i + T[i] <= N:
        dp[i] = max(dp[i+1], dp[i+T[i]] + P[i])
    else:
        dp[i] = dp[i+1]

print(dp[0])
