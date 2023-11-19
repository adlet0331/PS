import sys
input = sys.stdin.readline

N = int(input())
xarr = []
yarr = []
zarr = []
for i in range(N):
    x, y, z = map(int, input().split())
    xarr.append((x, i))
    yarr.append((y, i))
    zarr.append((z, i))
xarr.sort()
yarr.sort()
zarr.sort()

linkarr = []
roadarr = []
# x, y, z로 정렬해서 인접된 간선만 추려서 계산. N^2 로는 메모리 초과남
for i in range(N-1):
    roadarr.append((xarr[i+1][0]-xarr[i][0], xarr[i][1], xarr[i+1][1]))
    roadarr.append((yarr[i+1][0]-yarr[i][0], yarr[i][1], yarr[i+1][1]))
    roadarr.append((zarr[i+1][0]-zarr[i][0], zarr[i][1], zarr[i+1][1]))
roadarr.sort(reverse=True)
parentarr = [i for i in range(N)]

def find(v):
    if v == parentarr[v]:
        return v
    parentarr[v] = find(parentarr[v])
    return parentarr[v]

def unionnode(anode, bnode):
    p1 = find(anode)
    p2 = find(bnode)
    if p1 > p2:
        p1, p2 = p2, p1
    parentarr[p1] = p2

cnt = 0
lenval = 0
while cnt != N - 1:
    road = roadarr.pop()
    (costval, row, col) = road
    if find(row) == find(col):
        continue
    else:
        linkarr.append((row, col))
        unionnode(row, col)
        cnt += 1
        lenval += costval
print(lenval)
