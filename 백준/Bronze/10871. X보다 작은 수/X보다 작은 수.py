n, x = map(int, input().split())

m = list(map(int, input().split()))

for i in range(len(m)):
    if m[i] < x:
        print(m[i], end=" ")
