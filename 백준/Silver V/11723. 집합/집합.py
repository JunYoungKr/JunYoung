import sys
input = sys.stdin.readline

# 연산의 수 M
M = int(input())

S = set()
# print(S)
for _ in range(M):
    order = input().split()
    # print(order[0], order[1])

    # add
    if order[0] == "add":
        S.add(int(order[1]))
    # remove
    elif order[0] == "remove":
        try:
            S.remove(int(order[1]))
        except:
            pass
    # check
    elif order[0] == "check":
        if int(order[1]) in S:
            print("1")
        else:
            print("0")
    # toggle
    elif order[0] == "toggle":
        if int(order[1]) in S:
            S.remove(int(order[1]))
        else:
            S.add(int(order[1]))
    # all
    elif order[0] == "all":
        S = set([i for i in range(1, 21)])
    # empty
    elif order[0] == "empty":
        S = set()

    # print("S", S)
