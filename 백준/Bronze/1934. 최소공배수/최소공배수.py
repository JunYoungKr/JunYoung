import sys

N = int(input())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    aa, bb = a, b

    while a % b:
        a, b = b, a % b

    print(aa*bb // b)
