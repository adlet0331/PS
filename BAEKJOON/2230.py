import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()
# 투포인트?
start = 0
end = 1
result = 2000000000
while result > M and end < N and start < N - 1:
    if data[end] - data[start] < M:
        end += 1
    elif data[end] - data[start] > M:
        result = min(result, data[end] - data[start])
        start += 1
    else:
        result = M
        break
print(result)