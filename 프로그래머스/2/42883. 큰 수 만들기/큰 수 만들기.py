# number = "4177252841"
# k = 4


def solution(number, k):
    stack = []

    for i in number:
        if len(stack) == 0:
            stack.append(i)
            continue
        if k > 0:
            while stack[-1] < i:
                stack.pop()
                k -= 1
                if len(stack) == 0 or k <= 0:
                    break
        stack.append(i)
    # print(stack)
    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)


# print(solution(number, k))
