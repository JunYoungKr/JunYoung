import sys
input = sys.stdin.readline

# 현금
N = int(input())

준현 = N

stock = list(map(int, input().split()))
# print(stock)

# 준현이가 주식하는법

준현_주식수 = 0
# 준현이의 재산
for i in range(len(stock)):
    if stock[i] <= 준현:
        준현_주식수 += 준현 // stock[i]
        준현 = 준현 % stock[i]


준현_재산 = 준현_주식수 * stock[-1] + 준현
# print(준현_재산)


# 성민이가 주식하는법
# 성민이가 주식을 매입하는 날짜는 3일 연속 하락하고 다음 날 전량 매수함


# 성민이의 전략 변수 초기화
성민_잔돈 = N
성민_주식수 = 0

# 성민이의 주식 매수 및 매도 전략 실행
for i in range(len(stock) - 3):
    # 3일 연속 하락하면 전량 매수
    if stock[i] > stock[i+1] > stock[i+2] > stock[i+3]:
        성민_주식수 += 성민_잔돈 // stock[i+3]
        성민_잔돈 = 성민_잔돈 % stock[i+3]

    # 3일 연속 상승하면 전량 매도
    if stock[i] < stock[i+1] < stock[i+2] < stock[i+3]:
        성민_잔돈 += 성민_주식수 * stock[i+3]
        성민_주식수 = 0

# 마지막 날 주식을 가지고 있다면, 마지막 주식 가격으로 전량 매도
성민_잔돈 += 성민_주식수 * stock[-1]
성민_주식수 = 0

# 성민이의 최종 재산 출력
# print(성민_잔돈, 준현_재산)

if 성민_잔돈 > 준현_재산:
    print("TIMING")
elif 성민_잔돈 < 준현_재산:
    print("BNP")
else:
    print("SAMESAME")
