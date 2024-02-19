import sys
input = sys.stdin.readline

N = int(input())

arr = set(map(int, input().split()))

M = int(input())

arr2 = list(map(int, input().split()))

ans = []
for i in arr2:
    if i in arr:
        # ans.append(1)
        print(1)
    else:
        # ans.append(0)
        print(0)
# print(ans)
