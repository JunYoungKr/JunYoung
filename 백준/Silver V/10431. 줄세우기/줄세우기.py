import sys
input = sys.stdin.readline

# 테스트 케이스 P
P = int(input())

for _ in range(P):
    arr = list(map(int, input().split()))

    # 테스트케이스 번호
    num = arr[0]

    # 테스트케이스를 제외한 나머지 요소들을 집어넣은 새로운 List arr2
    arr1 = [arr[i] for i in range(1, 21)]
    # print("arr1:", arr1)

    # 교환 횟수
    total = 0

    for end in range(0, len(arr1)):
        for i in range(end, 0, -1):
            if arr1[i-1] > arr1[i]:
                arr1[i-1], arr1[i] = arr1[i], arr1[i-1]
                total += 1
    print(num, total)
