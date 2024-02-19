import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

# 테스트 케이스 T
T = int(input())

cnt = []
for _ in range(T):
    a = input()

    total = 0
    num = 0
    for i in range(len(a)):
        # O의 길이(count)를 재주다가 다음에 X가 나온다면 멈추면 길이를 0으로 초기화
        if a[i] == 'O':
            num += 1
            total += num
            if a[i+1] == 'X':
                num = 0
    print(total)
