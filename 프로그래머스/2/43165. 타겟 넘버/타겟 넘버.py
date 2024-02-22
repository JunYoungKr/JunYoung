def solution(numbers, target):
    answer = 0
    
    dp = [[] for _ in range(len(numbers) + 1)]

    dp[0].append(0)  # 시작점은 0에서 시작
    
    for i in range(len(numbers)):
        for prev_sum in dp[i]:
            dp[i+1].append(prev_sum + numbers[i])  # 현재 숫자를 더한 값을 추가
            dp[i+1].append(prev_sum - numbers[i])  # 현재 숫자를 뺀 값을 추가

    # dp의 마지막 리스트에서 target과 일치하는 값의 개수를 세어 answer에 할당
    answer = dp[-1].count(target)
    
    # print(dp)
    
    return answer