import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

arr2 = list(combinations_with_replacement(arr, M))

for i in arr2:
    for j in i:
        print(j, end=' ')
    print()
