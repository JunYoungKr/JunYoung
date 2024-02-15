import sys
input = sys.stdin.readline

H, W = map(int, input().split())

map = [list(map(str, input().strip())) for _ in range(H)]

flag = False
num = 1

for i in range(H):
    for j in range(W):
        if map[i][j] == 'c':
            map[i][j] = 0
            flag = True
            num = 1
        # 바로 전에 구름이 나오지 않은 경우
        elif map[i][j] == '.' and flag == False:
            map[i][j] = -1
        # 바로 전에 구름이 나온 경우
        elif map[i][j] == '.' and flag == True:
            map[i][j] = num
            num += 1
    # 초기화
    num = 1
    flag = False
    print(*map[i])
