import sys
input = sys.stdin.readline

# 테스트 케이스 T
T = int(input())

for _ in range(T):
    # 동전의 가지 수 N
    N = int(input())
    # 동전의 각 금액
    coins = list(map(int, input().split()))
    # 금액 M
    M = int(input())

    dp = [0]*(M+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]

    print(dp[M])
