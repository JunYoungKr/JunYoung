import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

# print(arr)

if M == 1:
    result = arr

else:
    arr2 = list(permutations(arr, M))

    result = [" ".join(map(str, i)) for i in arr2]


for i in range(len(result)):
    print(result[i])
