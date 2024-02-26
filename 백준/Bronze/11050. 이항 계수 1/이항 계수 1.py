import sys
import copy
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())

res1 = [i for i in range(1, N + 1)]
res2 = [i for i in range(1, K + 1)]
res3 = [i for i in range(1, (N-K) + 1)]

# print(res1)
# print(res2)
# print(res3)

ans1 = 1
for i in res1:
    ans1 *= int(i)

ans2 = 1
for i in res2:
    ans2 *= int(i)

ans3 = 1
for i in res3:
    ans3 *= int(i)

print(int((ans1/(ans2*ans3)) % 10007))
