n = int(input())

arr = list(map(int, input().split()))

# print(arr)
arr.sort()

sum_ = 0

for i in range(1, n+1):
    sum_ += sum(arr[0:i])

print(sum_)
