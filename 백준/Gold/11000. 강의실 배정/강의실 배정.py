import heapq
import sys
input = sys.stdin.readline

N = int(input())

# 첫 번째로 입력받음
arr = []
# print(arr)

for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()
# print(arr)

room = []
heapq.heappush(room, arr[0][1])

# print("room:", room)

for i in range(1, N):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

print(len(room))
