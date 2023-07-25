t = int(input())

for i in range(t):
    x, y = input().split()
    for j in y:
        print(j * int(x), end='')
    print()
