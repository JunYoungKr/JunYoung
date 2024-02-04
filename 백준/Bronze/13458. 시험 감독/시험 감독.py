import heapq
import sys
input = sys.stdin.readline

# 시험장의 개수 N
N = int(input())

# 각 시험장에 있는 응시자의 수 A
test = list(map(int, input().split()))
# print(test)

# B, C
B, C = map(int, input().split())

total = 0
for i in range(len(test)):
    test[i] -= B
    total += 1
    if test[i] > 0:
        if test[i] % C == 0:
            total += test[i] // C
        else:
            total += test[i] // C + 1

print(total)
