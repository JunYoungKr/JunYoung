import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

pocketmon = {}
number = {}

for i in range(1, N + 1):
    po = sys.stdin.readline().rstrip()
    pocketmon[i] = po
    number[po] = i

for i in range(M):
    x = sys.stdin.readline().rstrip()
    if x.isdigit():
        print(pocketmon[int(x)])
    else:
        print(number[x])
