import sys
import heapq
from itertools import permutations
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

# 강의 종료 시간을 기준으로 정렬
arr.sort(key=lambda x: (x[1], x[0]), reverse=False)
# print(arr)

count = 1
end_time = arr[0][1]

for i in range(1, N):
    # 첫 강의 종료시간보다 다음 강의 시작 시간이 빠르다면
    if arr[i][0] >= end_time:
        count += 1
        end_time = arr[i][1]

print(count)
