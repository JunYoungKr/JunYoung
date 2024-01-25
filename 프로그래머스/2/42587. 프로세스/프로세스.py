from collections import deque

# priorities = [2, 1, 3, 2]
# location = 2


def solution(priorities, location):
    answer = []
    # deque에 enumerate 함수를 사용하여 index값과 value를 함께 튜플 형태로 넣어준다.
    queue = deque((i, j) for i, j in enumerate(priorities))

    # print("queue:", queue)

    while queue:
        # queue의 맨 왼쪽 튜플을 뺀다
        num = queue.popleft()
        # print(num)
        
        # 그리고 비교를 한다
        # 만약에 꺼낸 우선순위보다 queue에 더 높은 우선순위가 있다면 다시 집어넣는다.
        if any(num[1] < q[1] for q in queue):
            queue.append(num)
            # print(queue)
        # 아니라면 answer에 넣는다.
        else:
            answer.append(num)
            # print(answer)
    # answer이라는 list를 순회하면서 location과 일치한 것이 있다면 list answer에서 index를 찾아 +1을 해주고 출력
    # 리스트 answer에서는 index가 0 1 2 3 이기때문에
    for i in answer:
        if i[0] == location:
            return answer.index(i)+1
    return answer


# print(solution(priorities, location))
