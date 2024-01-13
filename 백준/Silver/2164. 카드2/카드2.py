import sys
from collections import deque


N = int(sys.stdin.readline())

queue = deque([])

for i in range(1, N+1):
    queue.append(i)

# 첫 번째 요소를 뺌
# 그 다음에 있는 요소를 저장시킴과에 동시에 제거 후 맨 끝으로 확장

while len(queue) > 1:
    # print(len(queue))
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue[0])
