# arr = [1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4]

# a = arr.count(2)
# print(a)

n, m = map(int, (input().split()))

x = list(map(int, input().split()))

for i in (x):
    if i < m:
        print(i, end=" ")
