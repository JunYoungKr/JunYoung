from collections import deque
import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

모음 = ['a', 'e', 'i', 'o', 'u']

while True:
    a = input().strip()
    x = y = 0
    if a == 'end':
        # print("종료합니다")
        break
    모음_count = 0
    for i in 모음:
        # 모음 하나를 반드시 포함해야한다.
        if i in a:
            모음_count += 1
    # print(모음_count)

    # 모음이 하나도 없다면 not acceptable 출력
    if 모음_count < 1:
        print("<{}> is not acceptable.".format(a))
        continue

    # 모음이 연속 3개거나 자음만 연속 3개인 경우 체크
    for i in range(len(a)-2):
        if a[i] in 모음 and a[i+1] in 모음 and a[i+2] in 모음:
            x = 1
        elif not (a[i] in 모음) and not (a[i+1] in 모음) and not (a[i+2] in 모음):
            x = 1

    if x == 1:
        print("<{}> is not acceptable.".format(a))
        continue

    # 같은 글이 연속 두 개인지 체크, 그러나 e나 o면 continue
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            if a[i] == 'e' or a[i] == 'o':
                continue
            else:
                y = 1

    if y == 1:
        print("<{}> is not acceptable.".format(a))
        continue

    print("<{}> is acceptable.".format(a))
