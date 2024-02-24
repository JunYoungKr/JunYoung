# 지도의 크기 N 입력
N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input())))

# print(arr)


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    # 음료수 얼려먹기와 다르게 1을 count하는 것이므로 arr[x][y] == 1로 변경
    if arr[x][y] == 1:
        arr[x][y] = 0
        # 전역변수 global count 사용
        global count
        count += 1
        # 상
        dfs(x-1, y)
        # 하
        dfs(x+1, y)
        # 좌
        dfs(x, y-1)
        # 우
        dfs(x, y+1)
        return True
    return False


count = 0
arr_count = []
res = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            arr_count.append(count)
            count = 0
# 오름차순 출력
arr_count.sort()

print(len(arr_count))
for i in arr_count:
    print(i)
