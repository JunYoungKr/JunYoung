import sys
import heapq
from itertools import permutations
input = sys.stdin.readline

N = int(input())

roap = []
for _ in range(N):
    roap.append(int(input()))

roap.sort(reverse=True)  # 15 10으로 정렬됨
# print(roap)


ans = []

# 로프가 1개일 때 15*1 = 15, 2개일 때 10*2 = 20이므로 최대 중량은 20이다.
for i in range(N):
    ans.append(roap[i]*(i+1))
print(max(ans))
