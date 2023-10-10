import math

N = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, min(mid + 1, N + 1)):
        cnt += min(mid // i, N)
    
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
    