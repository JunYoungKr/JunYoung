# array = [1, 5, 2, 6, 3, 7, 4]

# print(sorted(arr[1:5])[2])


def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
