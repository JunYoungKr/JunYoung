import heapq
import sys
input = sys.stdin.readline

# 테스트 케이스 T
T = int(input())

# 지원자의 숫자 N
for _ in range(T):
    N = int(input())

    # N개 줄에 각각 지원자의 서류심자 성적, 면접 성적의 순위가 공백을 두고 한 줄에 입력
    grade = [list(map(int, input().split())) for _ in range(N)]
    grade.sort()

    # 최대로 합격할 수 있는 지원자 수
    count = 1
    max_ = grade[0][1]
    for i in range(1, N):
        if max_ > grade[i][1]:
            count += 1
            max_ = grade[i][1]
    print(count)
