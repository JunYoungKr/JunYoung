n = int(input())

for _ in range(n):
    charge = int(input())
    for i in [25, 10, 5, 1]:
        print(charge // i, end=' ')
        charge %= i
