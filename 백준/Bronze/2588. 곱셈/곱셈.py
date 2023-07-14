import math

A = int(input())
B = int(input())

print(A * (B % 10))
print(A * math.floor(B % 100 / 10))
print(A * math.floor(B / 100))
print(A * B)
