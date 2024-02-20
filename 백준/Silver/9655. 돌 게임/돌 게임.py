from collections import deque
import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
if N % 2 == 0:
    print('CY')
else:
    print('SK')
