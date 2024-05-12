R, C = map(int, input().split())
def chartobint(char):
    return 1 << (ord(char) - 65)
mdata = []
for _ in range(R):
    mdata.append(input())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
findlist = [(chartobint(mdata[0][0]), (0, 0), 1)]
cnt = 0
while findlist:
    cstr, (i, j), ccnt = findlist.pop()
    cnt = max(cnt, ccnt)
    for (ii, jj) in directions:
        ni, nj = i + ii, j + jj
        if ni < 0 or nj < 0 or ni >= R or nj >= C or (chartobint(mdata[ni][nj]) & cstr):
            continue
        if (cstr | chartobint(mdata[ni][nj]), (ni, nj)) not in findlist:
            findlist.append((cstr | chartobint(mdata[ni][nj]), (ni, nj), ccnt + 1))
print(cnt)