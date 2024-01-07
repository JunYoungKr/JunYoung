N = int(input())

num = 0
for i in range(N):
    # print(1 + 2 ** i)
    num = 1 + 2 ** (i + 1)

print(num**2)
