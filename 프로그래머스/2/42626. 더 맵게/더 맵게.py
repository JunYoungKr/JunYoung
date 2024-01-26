import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        조합 = first + second * 2
        heapq.heappush(scoville, 조합)

        if (len(scoville) == 2) and (scoville[0] + scoville[1] * 2) < K:
            return -1
        # print(first, second)
    return answer