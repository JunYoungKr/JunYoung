import sys


def isPrime(x):
    if x == 1 or x == 0:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
    return True


M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
