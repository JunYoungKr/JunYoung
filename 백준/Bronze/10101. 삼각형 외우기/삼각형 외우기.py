arr = []

for i in range(3):
    x = int(input())
    arr.append(x)

for i in range(len(arr)):
    if arr.count(60) == 3:
        print("Equilateral")
        break
    elif sum(arr) == 180 and (arr[i] == arr[i+1] or arr[i+1] == arr[i+2] or arr[i] == arr[i+2]):
        print("Isosceles")
        break
    elif sum(arr) == 180 and (arr[i] != arr[i+1] or arr[i+1] != arr[i+2] or arr[i] != arr[i+2]):
        print("Scalene")
        break
    elif sum(arr) != 180:
        print("Error")
        break
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

