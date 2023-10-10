import sys
input = sys.stdin.readline

N, M = map(int, input().split())
datalist = list(map(int, input().split()))

maxval = 0
for d in datalist:
    if d > maxval:
        maxval = d

start = 0
end = maxval

while start + 1 != end:
    mid = (start + end) // 2
    cnt = 0
    for d in datalist:
        cnt += max(0, d - mid)
    if cnt >= M:
        start = mid
    else:
        end = mid

ecnt = 0
for d in datalist:
    ecnt += max(0, d - end)
if ecnt > M:
    print(end)
else:
    print(start)