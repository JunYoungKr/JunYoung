import math
def solution(progresses, speeds):
    answer = []
    
    days = []

    for i in range(len(progresses)):
        days = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]

    for i in range(len(days)-1):
        if days[i] > days[i+1]:
            days[i+1] = days[i]

    counter = {}

    for i in days:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    answer = list(counter.values())

    return answer