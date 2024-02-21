import sys
input = sys.stdin.readline

N, M = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [0] * (M+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, M+1):
        dp[i] += dp[i-coin]

print(dp[M])
