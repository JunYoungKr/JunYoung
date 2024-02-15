import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

car = [0] * 100
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        car[i] += 1
    # print(car)

total = 0
for i in range(len(car)):
    if car[i] == 0:
        total += 0
    elif car[i] == 1:
        total += A
    elif car[i] == 2:
        total += B * 2
    elif car[i] == 3:
        total += C * 3

print(total)
