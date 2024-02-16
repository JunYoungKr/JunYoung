import sys
input = sys.stdin.readline

# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 3번을 받았다면 3,6 번의 스위치의 상태를 바꿈

# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
# 그 구간에 속한 스위치의 상태를 모두 바꾼다


# 스위치 개수
N = int(input())

# 스위치 상태 입력
# 켜져있으면 1, 꺼져있으면 0
status = [-1] + list(map(int, input().split()))

# 학생 수 입력 (100 이하 양의 정수)
student = int(input())


def change(num):
    if status[num] == 0:
        status[num] = 1
    else:
        status[num] = 0
    return


for _ in range(student):
    # 학생의 성별, 학생이 받은 수
    # 남자 1, 여자 2
    gender, number = map(int, input().split())
    # print("gender, number", gender, number)
    # 남자인 경우
    if gender == 1:
        for i in range(len(status)):
            # print(i, end=' ')
            # 배수라면
            if i % number == 0:
                if status[i] == 0:
                    status[i] = 1
                else:
                    status[i] = 0
    # 여자인 경우
    elif gender == 2:
        change(number)
        for j in range(N // 2):
            if number + j > N or number - j < 1:
                break
            # 좌우가 같을 경우
            if status[number+j] == status[number-j]:
                change(number+j)
                change(number-j)
            # 좌우가 다른 경우, break
            else:
                break

# 20씩 나눠 print
for i in range(1, N + 1):
    print(status[i], end=' ')
    if i % 20 == 0:
        print()
