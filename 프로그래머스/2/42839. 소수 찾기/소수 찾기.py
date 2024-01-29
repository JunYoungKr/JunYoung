from itertools import permutations


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    unique_numbers = set()

    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int(''.join(p))
            unique_numbers.add(num)

    # print(unique_numbers)
    count = 0
    for i in unique_numbers:
        if isPrime(i):
            count += 1
    return count


# numbers = "011"
# print(solution(numbers))
