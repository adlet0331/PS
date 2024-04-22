# N = 5000
N = int(input())
data = list(map(int, input().split()))
data.sort()
# 첫 plus 위치
firstpindex = -1
for i in range(N):
    if data[i] > 0:
        firstpindex = i
# 투 포인터 2번, mstart, mend, pend / mstart, pstart, pend
# O(N ^ 2) * 2 = 2500 * 2500 * 2 = 1.25 * 10^7
for pindex in range(firstpindex, N):
    