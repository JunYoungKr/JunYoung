from collections import deque
# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    limit = len(queue1) * 4

    # q1의 합
    sum_q1 = sum(queue1)
    # q2의 합
    sum_q2 = sum(queue2)

    total = sum_q1 + sum_q2
    # print(total)

    if total % 2 != 0:
        return -1

    while True:
        # q1의 합 > q2의 합
        if sum_q1 > sum_q2:
            num = queue1.popleft()
            queue2.append(num)
            sum_q1 -= num
            sum_q2 += num
            answer += 1
        # q1의 합 < q2의 합
        elif sum_q1 < sum_q2:
            num = queue2.popleft()
            queue1.append(num)
            sum_q1 += num
            sum_q2 -= num
            answer += 1
        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer


# print(solution(queue1, queue2))
