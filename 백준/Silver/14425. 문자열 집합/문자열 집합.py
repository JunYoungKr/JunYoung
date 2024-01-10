import sys

N, M = map(int, sys.stdin.readline().split())

S = []
count = 0

for _ in range(N):
    a = input()
    S.append(a)

for _ in range(M):
    b = input()
    if b in S:
        count += 1

print(count)
