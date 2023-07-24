N = int(input())

x = list(map(int, input().split()))

# 최댓값
M = 0

for i in x:
    if M < i:
        M = i

y = []

for i in x:
    y.append(i / M * 100)

sum = 0
for i in y:
    sum += i

print(sum / N)
