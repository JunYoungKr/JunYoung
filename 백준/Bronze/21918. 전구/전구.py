import sys
import copy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

switch = [0]+list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())

    # b번째 전구의 상태를 c로 변경한다
    if a == 1:
        switch[b] = c

    # b부터 c번째까지의 전구의 상태를 변경한다.
    elif a == 2:
        for i in range(b, c+1):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    # b부터 c번까지의 전구를 끈다 (상태 0)
    elif a == 3:
        for i in range(b, c+1):
            if switch[i] == 1:
                switch[i] = 0
    # b부터 c번까지의 전구를 킨다 (상태 1)
    elif a == 4:
        for i in range(b, c+1):
            if switch[i] == 0:
                switch[i] = 1
    # print(switch)

for i in range(1, N+1):
    print(switch[i], end=' ')
