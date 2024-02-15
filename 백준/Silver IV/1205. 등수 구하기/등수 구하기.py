import sys
input = sys.stdin.readline

# N, 태수의 새로운 점수, 랭킹 리스트에 올라갈 수 있는 점수의 개수 P
N, new_score, P = map(int, input().split())

# 10 <= P <= 50
# 0 <= N <= P

arr = list(map(int, input().strip().split()))
# print(arr)


# 새로운 점수를 arr에 추가해준다
arr.append(new_score)
# print(arr)

# 점수를 추가해준 후 정렬을 한다
arr.sort(reverse=True)  # 100 90 90 80
# print(arr)

rank = [1] * len(arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            rank[i] += 1

# print(rank)

# 랭킹리스트에 올라갈 수 없을 정도로 낮다 -> 마지막 숫자보다 작거나 같고 리스트에 추가했을때 리스트의 길이 (N) > P 일때
if new_score <= arr[-1] and len(arr) > P:
    print(-1)
else:
    for i in range(len(arr)):
        if arr[i] == new_score:
            print(i+1)
            break
