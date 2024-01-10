import sys

N, M = map(int, sys.stdin.readline().split())

S = dict()
count = 0

for _ in range(N):
    a = sys.stdin.readline()
    S[a] = True

for _ in range(M):
    b = sys.stdin.readline()
    if b in S.keys():
        count += 1

print(count)
