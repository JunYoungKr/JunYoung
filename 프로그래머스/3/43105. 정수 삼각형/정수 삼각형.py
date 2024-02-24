def solution(triangle):
    answer = 0
    
    triangle[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle)):
            if j == 0:
                triangle[i][0] += triangle[i-1][0]
            elif i == j:
                triangle[i][j] += triangle[i-1][j-1]
    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i])-1):
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if triangle[i][j] > answer:
                answer = triangle[i][j] 
    return answer