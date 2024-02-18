import sys
import math
from itertools import permutations
input = sys.stdin.readline

# 테스트 케이스 T
T = int(input())

for _ in range(T):
    arr = []
    N = int(input())

    for i in range(N):
        # 서류 성적, 면접 성적
        arr.append(list(map(int, input().split())))
    # print(arr)
    arr.sort(key=lambda x: x[0])
    # print(arr)

    count = 1
    num = arr[0][1]
    for i in range(1, N):
        if arr[i][1] < num:
            count += 1
            num = arr[i][1]
    print(count)
