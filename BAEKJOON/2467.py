from collections import deque

N = int(input())
# N = 100,000
data = list(map(int, input().split()))
data = deque(data)

cnt = 10000000000
result = (0, 0)
left = data.popleft()
right = data.pop()
while True:
    sum = left + right
    if abs(sum) < cnt:
        cnt = abs(sum)
        result = (left, right)
    if sum == 0 or not data:
        break
    if sum > 0:
        right = data.pop()
    elif sum < 0:
        left = data.popleft()
print(f"{result[0]} {result[1]}")