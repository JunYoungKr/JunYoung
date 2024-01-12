import sys

N = int(sys.stdin.readline())

arr = []

for i in range(N):
    order = list(map(int, sys.stdin.readline().split()))
    if order[0] == 1:
        # 정수를 스택에 넣는다
        arr.append(order[1])
        # print("arr:", arr)
    elif order[0] == 2:
        # 스택에 정수가 있다면
        if arr:
            # 맨 위의 정수를 뺴고 출력
            print(arr.pop())
            # print("arr:", arr)
            # 없다면 -1을 대신 출력
        else:
            print(-1)
        # 스택에 들어있는 정수의 개수를 출력한다
    elif order[0] == 3:
        print(len(arr))
    elif order[0] == 4:
        # 스택이 비어있으면 1
        if arr:
            print(0)
        # 아니면 0을 출력한다
        else:
            print(1)
    elif order[0] == 5:
        # 스택에 정수가 있다면 맨 위의 정수를 출력한다.
        if arr:
            print(arr[-1])
        # 없다면 -1을 출력
        else:
            print(-1)
