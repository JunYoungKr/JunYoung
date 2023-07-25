abc = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

x = input()

total_time = 0

# abc를 한 개씩 분리
for i in abc:
    # abc 를 하나씩 또 분리
    for j in i:
        # 입력받은 x를 한 개씩 분리
        for k in x:
            # 분리한 것들끼리 일치한다면 abc의 index + 3을 총 시간에 더한다
            if j == k:
                total_time += abc.index(i) + 3

print(total_time)
