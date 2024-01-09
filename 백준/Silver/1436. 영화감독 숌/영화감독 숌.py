N = int(input())

res = 666
count = 0

while True:
    if '666' in str(res):
        count += 1
        if count == N:
            break
    res += 1

print(res)
