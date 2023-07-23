# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# print(sorted(participant))
# print(sorted(completion))


def solution(participant, completion):
    answer = ''

    # sort 함수를 통해 정렬
    participant.sort()
    completion.sort()

    # 완주자 list의 길이만큼 돌면서 이미 정렬을 한 상태이기 때문에 일치하지 않는다면 그것이 정답
    # 일치한다면 완주했다는 뜻이기 때문에 반복문 + 1
    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            answer = participant[i]
            break

    # ['eden', 'kiki', 'leo']
    # ['eden', 'kiki'] 이런 식으로 정렬이 된 상태이기 때문에
    # 아직 정답을 찾지 못한 경우 list의 마지막 요소가 정답이다

    if answer == '':
        answer = participant[len(participant)-1]

    return answer
