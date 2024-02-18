import sys
input = sys.stdin.readline

# 수열의 길이 N
N = int(input())

# 음수
minus = []
# 양수
plus = []
# 0
zero = []

res = 0

for _ in range(N):
    a = int(input())
    if a <= 0:
        minus.append(a)
    elif a > 1:
        plus.append(a)
    else:
        res += a


plus.sort(reverse=True)
minus.sort()

for i in range(0, len(minus), 2):
    if i + 1 >= len(minus):
        res += minus[i]
    else:
        res += minus[i] * minus[i+1]


for i in range(0, len(plus), 2):
    if i + 1 >= len(plus):
        res += plus[i]
    else:
        res += plus[i] * plus[i+1]
print(res)
