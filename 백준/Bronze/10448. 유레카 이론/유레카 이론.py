import sys
input = sys.stdin.readline

triangle = [n*(n+1)//2 for n in range(1, 46)]
# print(triangle)

Eureka = [0] * 1001

for i in triangle:
    for j in triangle:
        for k in triangle:
            if i + j + k <= 1000:
                Eureka[i + j + k] = 1


# 테스트케이스 T
T = int(input())

for _ in range(T):
    print(Eureka[int(input())])
