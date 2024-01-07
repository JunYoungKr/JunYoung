N = int(input())

num = 2
number = []

while N > 1:
    if N % num == 0:
        number.append(num)
        N //= num
    else:
        num += 1

for i in number:
    print(i, end='\n')
