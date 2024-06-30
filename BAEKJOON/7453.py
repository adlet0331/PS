N = int(input())
data = [[], [], [], []]
for _ in range(N):
    ilist = list(map(int, input().split()))
    for i in range(4):
        data[i].append(ilist[i])
# N = 4000
# 16 * 10^6
# 2개씩 합쳐서 2개의 dictionary로 만들기
adict = {}
bdict = {}
for i in range(N):
    for j in range(N):
        anum = data[0][i] + data[1][j]
        if anum in adict:
            adict[anum] += 1
        else:
            adict[anum] = 1
        bnum = data[2][i] + data[3][j]
        if bnum in bdict:
            bdict[bnum] += 1
        else:
            bdict[bnum] = 1
cnt = 0
for key, value in adict.items():
    cnt += value * bdict.get(-key, 0)
print(cnt)