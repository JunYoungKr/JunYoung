

while True:
    arr = []
    x, y, z = (map(int, input().split()))
    # 세 변의 길이가 모두 같은 경우
    arr.append(x)
    arr.append(y)
    arr.append(z)
    if x == 0 and y == 0 and z == 0:
        break
    if (x + y <= z) or (x + z <= y) or (y + z <= x):
        print("Invalid")
        continue
    # print(arr)
    if len(set(arr)) == 1:
        print("Equilateral")
    # 두 변의 길이가 같은 경우
    elif len(set(arr)) == 2:
        print("Isosceles")
    # 세 변의 길이가 모두 다른 경우
    elif len(set(arr)) == 3:
        print("Scalene")
