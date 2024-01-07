N = int(input())

arr = list(map(int, input().split()))

count = 0

for num in arr:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1

print(count)
