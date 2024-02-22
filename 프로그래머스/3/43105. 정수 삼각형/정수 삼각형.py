def solution(triangle):
    answer = 0
    
    # 첫 자리 더해주기
    triangle [0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        
    # 끝 자리 더해주기
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if i == j:
                triangle[i][j] += triangle[i-1][j-1]
    # print(triangle)
    
    # 첫 과 끝 사이 최댓값으로 비교해서 더해주기
    for i in range(1,len(triangle)):
        for j in range(1,len(triangle[i])-1):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
    answer = 0
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if answer < triangle[i][j]:
                answer= triangle[i][j]
    return answer