N = list(input())
N = sorted(N, reverse=True)
# print(N)

# 3의 배수가 아니라는 뜻이니까
if N[-1] != '0':
    print(-1)
else:
    sum = 0
    for i in N:
        sum += int(i)
        # print(sum, i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(N))
