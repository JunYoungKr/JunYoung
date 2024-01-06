N, B = input().split()

abc = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]

res = 0

for i, n in enumerate(N):
    # print(i, n)
    # print(abc.index(n))
    res += abc.index(n) * int(B) ** i

print(res)
