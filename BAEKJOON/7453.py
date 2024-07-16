N = int(input())
data = [[], [], [], []]
for _ in range(N):
    ilist = list(map(int, input().split()))
    for i in range(4):
        data[i].append(ilist[i])
# data는 int 범위
# N = 4000
# 16 * 10^6
# dictionary in 연산 10 ^ 8 -> O(1)
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
cnt = 0
for i in range(N):
    for j in range(N):
        bnum = data[2][i] + data[3][j]
        cnt += adict.get(-bnum, 0)
print(cnt)