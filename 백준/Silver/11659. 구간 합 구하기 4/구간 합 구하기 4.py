from collections import deque
import sys
from itertools import accumulate
input = sys.stdin.readline


N, M = map(int, input().split())

arr = list(map(int, input().split()))

sum_arr = [0]

temp = 0
for i in arr:
    temp += i
    sum_arr.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j]-sum_arr[i-1])
