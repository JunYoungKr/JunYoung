def solution(arr):
    answer = []
    # 첫 번째 요소는 비교 대상이 없기 때문에 무조건 answer에 추가
    answer.append(arr[0])

    for i in range(1, len(arr)):
        # 이전 요소(arr[i-1])와 현재 요소(arr[i])가 다르다면 answer에 추가
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer
