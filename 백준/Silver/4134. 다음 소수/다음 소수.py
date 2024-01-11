import sys


def isPrime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


N = int(sys.stdin.readline())

for i in range(N):
    a = int(sys.stdin.readline())
    while True:
        if a == 0 or a == 1:
            print(2)
            break
        if isPrime(a):
            print(a)
            break
        else:
            a += 1
