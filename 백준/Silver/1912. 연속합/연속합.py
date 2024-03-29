import sys
input = sys.stdin.readline


N = int(input())
dp = [0] * N

arr = list(map(int, input().split()))

dp[0] = arr[0]

for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))
