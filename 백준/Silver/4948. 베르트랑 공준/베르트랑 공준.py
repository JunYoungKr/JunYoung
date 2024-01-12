import sys


def isPrime(x):
    if x == 1 or x == 0:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
    return True


arr = []
for i in range(2, 246912):
    if isPrime(i):
        arr.append(i)

# print(arr) 확인되었음

while True:
    count = 0
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in arr:
        if n < i <= 2 * n:
            count += 1

    print(count)
