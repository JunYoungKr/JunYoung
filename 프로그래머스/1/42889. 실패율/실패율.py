def solution(N, stages):
    answer = []
    failure = {}
    분모 = len(stages)
    
    for i in range(1, N +1):
        분자 = stages.count(i)
        if 분자 == 0:
            failure[i] = 0
        else:
            print(분자,"/" ,  분모)
            failure[i] = 분자 / 분모
            분모 -= 분자
    # print(failure)
    answer = sorted(failure, key=lambda x : failure[x], reverse=True)
            
    return answer