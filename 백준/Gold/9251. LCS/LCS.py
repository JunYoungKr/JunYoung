import sys
input = sys.stdin.readline

arr1 = input().strip()
arr2 = input().strip()

dp = [0] * (len(arr2))
# print(dp)

for i in range(len(arr1)):
    count = 0
    for j in range(len(arr2)):
        if count < dp[j]:
            count = dp[j]
        elif arr1[i] == arr2[j]:
            dp[j] = count + 1

print(max(dp))
