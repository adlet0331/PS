N, M, R = map(int, input().split())
mdata = []
for _ in range(N):
    mdata.append(list(map(int, input().split())))
# 시계방향 회전
newmdata = [[0 for _ in range(M)] for _ in range(N)]
# 테두리 개수, 테두리 내 index 개수
skincnt, skintotcntlist = min(N, M)//2, [0 for _ in range(min(N, M)//2)]
for i in range(skincnt):
    skintotcntlist[i] = (N + M) * 2 - 4 - 8 * i
skinindexlist = [[] for _ in range(skincnt)]
for i in range(skincnt):
    row, col = i, i
    for j in range(M - 2 * i - 1):
        skinindexlist[i].append((row, col))
        col += 1
    for j in range(N - 2 * i - 1):
        skinindexlist[i].append((row, col))
        row += 1
    for j in range(M - i * 2 - 1):
        skinindexlist[i].append((row, col))
        col -= 1
    for j in range(N - 2 * i - 1):
        skinindexlist[i].append((row, col))
        row -= 1
for i in range(skincnt):
    rotnum = R % skintotcntlist[i]
    for j in range(skintotcntlist[i]):
        (crow, ccol) = skinindexlist[i][j]
        (nrow, ncol) = skinindexlist[i][(j - rotnum) % skintotcntlist[i]]
        newmdata[nrow][ncol] = mdata[crow][ccol]
for mlist in newmdata:
    print(*mlist, sep=" ")