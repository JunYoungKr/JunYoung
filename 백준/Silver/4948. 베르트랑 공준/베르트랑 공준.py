import sys

count = 0


def isPrime(x):
    if x == 1 or x == 0:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
    return True


all_list = list(range(2, 246912))
memo = []

for i in all_list:
    if isPrime(i):
        memo.append(i)

while True:
    count = 0
    N = int(sys.stdin.readline())
    if N == 0:
        break
    next_N = 2 * N
    for i in memo:
        if N < i <= 2*N:
            count += 1
    print(count)
