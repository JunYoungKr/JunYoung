import sys

N, M = map(int, sys.stdin.readline().split())

a = list(map(int, (sys.stdin.readline().split())))

b = list(map(int, (sys.stdin.readline().split())))

a = set(a)
b = set(b)


print(len(a-b) + len(b - a))
