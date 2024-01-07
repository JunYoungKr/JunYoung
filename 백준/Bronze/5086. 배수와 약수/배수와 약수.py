while True:
    N, M = map(int, input().split())
    # 약수라면 flag = 1, 배수라면 flag = 2, 둘 다 아니라면 flag = 3
    if N == 0 and M == 0:
        break
    # 첫 번째 숫자가 두 번째 숫자의 약수이다.
    if M % N == 0:
        print("factor")
    # 첫 번째 숫자가 두 번째 숫자의 배수이다.
    elif N % M == 0:
        print("multiple")
    # 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
    else:
        print("neither")
