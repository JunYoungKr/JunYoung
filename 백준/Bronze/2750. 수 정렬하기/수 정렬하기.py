N = int(input())

arr = []
for i in range(N):
    a = int(input())
    arr.append(a)

arr = sorted(arr)

for i in arr:
    print(i)
