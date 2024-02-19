import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dp = [1] * 10

for i in range(1, N):
    for j in range(1, 10):
        dp[j] += dp[j-1]
    # print(dp)
print(sum(dp) % 10007)
