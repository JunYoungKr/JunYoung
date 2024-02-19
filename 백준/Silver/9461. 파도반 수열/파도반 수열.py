import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

# 테스트 케이스 T
T = int(input())

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

for i in range(T):
    a = int(input())
    print(dp[a])
