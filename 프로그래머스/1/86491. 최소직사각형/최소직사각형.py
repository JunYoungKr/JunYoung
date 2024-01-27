def solution(sizes):
    # 각 카드마다 가로와 세로 중 더 큰 값을 가로로 설정
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    # 최대 가로 길이와 최대 세로 길이를 찾음
    max_width = max(size[0] for size in sizes)
    max_height = max(size[1] for size in sizes)

    # 최대 가로 길이와 최대 세로 길이를 곱하여 답을 구함
    answer = max_width * max_height
    return answer


# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# print(solution(sizes))
