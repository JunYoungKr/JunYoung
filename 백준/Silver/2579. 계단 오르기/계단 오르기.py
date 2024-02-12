import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * 301

for i in range(1, N + 1):
    stairs[i] = int(input())
# print(stairs)
dp = [0] * 301
# 계단이 1개인 경우
dp[1] = stairs[1]

# 계단이 2개인 경우
dp[2] = stairs[2] + stairs[1]

# 계단이 3개인 경우
dp[3] = max(stairs[3] + stairs[2], stairs[1] + stairs[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

# print(dp)
print(dp[N])
