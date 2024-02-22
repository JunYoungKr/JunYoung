def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        slice = sorted(array[i-1:j])
        answer.append(slice[k-1])
    return answer
