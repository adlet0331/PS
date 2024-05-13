# N 10^6, M 10^4, K 10^4
import sys
input = sys.stdin.readline
print = sys.stdout.write
N, M, K = map(int, input().split())
data = [1]
for _ in range(N):
    data.append(int(input()))
segtree = [1 for _ in range(N*4)]

def makesegtree(start, end, cindex):
    if start == end:
        segtree[cindex] = data[start]
    else:
        mid = (start + end) // 2
        segtree[cindex] = (makesegtree(start, mid, cindex * 2) * makesegtree(mid + 1, end, cindex * 2 + 1)) % 1000000007
    return segtree[cindex]

def findpartmult(start, end, sindex, eindex, cindex):
    if eindex < start or sindex > end:
        return 1
    if start <= sindex and eindex <= end:
        return segtree[cindex]
    mindex = (sindex + eindex) // 2
    return findpartmult(start, end, sindex, mindex, cindex * 2) * findpartmult(start, end, mindex + 1, eindex, cindex * 2 + 1) % 1000000007

def fixpartmult(start, end, cindex, changeidx):
    if end < changeidx or start > changeidx:
        return segtree[cindex]
    
    if start == end:
        segtree[cindex] = data[start]
        return segtree[cindex]
    mindex = (start + end) // 2
    segtree[cindex] = fixpartmult(start, mindex, cindex * 2, changeidx) * fixpartmult(mindex + 1, end, cindex * 2 + 1, changeidx) % 1000000007
    return segtree[cindex]

makesegtree(1, N, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        data[b] = c
        fixpartmult(1, N, 1, b)
    if a == 2:
        print(f"{findpartmult(b, c, 1, N, 1)}\n")
