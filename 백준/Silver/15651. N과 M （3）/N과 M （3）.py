import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

arr2 = list(product(arr, repeat=M))

for i in arr2:
    for j in i:
        print(j, end=' ')
    print()
