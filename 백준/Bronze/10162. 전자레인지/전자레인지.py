# k개의 로프, 중량이 w인 물체를 들어올림

T = int(input())

if T % 10 != 0:
    print(-1)

else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)
