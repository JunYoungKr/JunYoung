import sys

N = int(sys.stdin.readline())

cards = list(map(int, input().split()))

M = int(sys.stdin.readline())

candidate = list(map(int, input().split()))


count = {}

for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

# print(count)

for i in candidate:
    res = count.get(i)
    if res == None:
        print(0, end=" ")
    else:
        print(res, end=" ")
