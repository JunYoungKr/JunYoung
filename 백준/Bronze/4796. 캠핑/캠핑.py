import sys
input = sys.stdin.readline


i = 0
while True:
    i += 1
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    # L, P, V가
    # 5, 8, 20일때
    # 8일 중 5일 동안만 사용가능, V일 짜리 휴가
    a = V // P
    b = V % P
    if L < b:
        b = L
    print("Case %d: %d" % (i, a * L + b))
