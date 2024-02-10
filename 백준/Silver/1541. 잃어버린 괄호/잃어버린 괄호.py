from itertools import combinations
import sys
input = sys.stdin.readline

arr = input().strip().split('-')

# print(arr)

num = []

for i in arr:
    sum = 0
    arr2 = i.split('+')
    for j in arr2:
        sum += int(j)
    num.append(sum)
# print(num)

total = num[0]
for i in range(1, len(num)):
    total -= num[i]

print(total)
