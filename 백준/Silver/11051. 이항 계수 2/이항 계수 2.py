import sys
import math
from collections import Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
print(int(math.comb(N, K) % 10007))
