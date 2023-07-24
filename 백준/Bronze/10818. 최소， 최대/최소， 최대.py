# arr = [1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4]

# a = arr.count(2)
# print(a)

n = int(input())

x = list(map(int, input().split()))

max = -1000000
min = 1000000
for i in x:
    if max < i:
        max = i
    if min > i:
        min = i

print(min, max)
