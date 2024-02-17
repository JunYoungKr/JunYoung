import sys
input = sys.stdin.readline


# 보드의 크기 N
N = int(input())

board = [list(map(str, input().strip())) for _ in range(N)]

# print()

# print(board)

result = 0


def check(board):
    max_count = 1

    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        count = 1
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    return max_count


for i in range(N):
    for j in range(N):
        if j + 1 < N:
            # 먼저 행 요소를 바꿔줌
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            count = check(board)
            result = max(result, count)
            # 그 다음에 검사 후 다시 바꿔줌
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i + 1 < N:
            # 먼저 행 요소를 바꿔줌
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            count = check(board)
            result = max(result, count)
            # 그 다음에 검사 후 다시 바꿔줌
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(result)
