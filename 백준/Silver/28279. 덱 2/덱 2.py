import sys
from collections import deque

deque = deque([])

N = int(sys.stdin.readline())

for i in range(N):
    order = list(map(int, (sys.stdin.readline().split())))
    if order[0] == 1:
        deque.appendleft(order[1])
        # print(deque)
    elif order[0] == 2:
        deque.append(order[1])
        # print(deque)
    elif order[0] == 3:
        if len(deque) >= 1:
            print(deque.popleft())
        else:
            print(-1)
    elif order[0] == 4:
        if len(deque) >= 1:
            print(deque.pop())
        else:
            print(-1)
    elif order[0] == 5:
        print(len(deque))
    elif order[0] == 6:
        if len(deque) >= 1:
            print(0)
        else:
            print(1)
    elif order[0] == 7:
        if len(deque) >= 1:
            print(deque[0])
        else:
            print(-1)
    elif order[0] == 8:
        if len(deque) >= 1:
            print(deque[-1])
        else:
            print(-1)
