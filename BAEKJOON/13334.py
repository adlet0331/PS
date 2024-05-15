import sys, heapq
input = sys.stdin.readline
# N 10^6, L 10^9
N = int(input())
pdata = []
for _ in range(N):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    pdata.append((a, b))
L = int(input())
pdata.sort()
result = 0
fheap = []
cstart, cend, cnt = pdata[0][0] - L, pdata[0][0], 0
for end, start in pdata:
    cend = end
    cstart = cend - L
    heapq.heappush(fheap, start)
    cnt += 1
    while fheap and fheap[0] < cstart:
        heapq.heappop(fheap)
        cnt -= 1
    result = max(result, cnt)
print(result)