'''
N = 1000
W = 1000

dp = 2 * 1000
O (N ^ 2) 까지 가능
과거를 다 돌아보자

아이디어 1
- dp[i][0], dp[i][1]: i번 사건을 1번 경찰차, 2번 경찰차가 해결 한경우 상태 저장

아이디어 2 (컨닝)
- dp[a][b]: 1번 경찰차가 마지막으로 a번, 2번 경찰차가 마지막으로 b를 해결한 최소 경로 (cnt) 저장
'''

N = int(input())
num = int(input())
data = [(-1, -1)]
for _ in range(num):
    data.append(list(map(int, input().split(" "))))

def getdist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 아이디어 2
# 사각형 껍질을 채워가는 느낌
dp = [[0 for _ in range(num + 1)] for _ in range(num + 1)]
checked = [[0 for _ in range(num + 1)] for _ in range(num + 1)]
dp[1][0] = getdist((1,1), data[1])
dp[0][1] = getdist((N,N), data[1])
for i in range(2, num + 1):
    cpos = data[i]
    # i 현재 탐색중인 사건
    # bindex: 사건 해결 X 하는 다른 경찰차 사건 번호
    # bbindex: 사건 해결 O 하는 경찰차가 있었던 이전 사건 번호
    for bindex in range(i):
        ccnt = 10000000
        rcnt = 10000000
        for bbindex in range(i):
            if bbindex == bindex or (bindex != i-1 and bbindex != i-1):
                continue
            bccnt = ccnt
            brcnt = rcnt
            if bbindex == 0:
                ccnt = min(ccnt, dp[0][bindex] + getdist(cpos, (1, 1)))
                rcnt = min(rcnt, dp[bindex][0] + getdist(cpos, (N, N)))
            else:
                ccnt = min(ccnt, dp[bbindex][bindex] + getdist(cpos, data[bbindex]))
                rcnt = min(rcnt, dp[bindex][bbindex] + getdist(cpos, data[bbindex]))
            if bccnt != ccnt:
                checked[i][bindex] = bbindex
            if brcnt != rcnt:
                checked[bindex][i] = bbindex
        dp[i][bindex] = ccnt
        dp[bindex][i] = rcnt
minlen = 1000000000
a, b = 0, 0
for i in range(num):
    if dp[num][i] < minlen:
        minlen = dp[num][i]
        a, b = num, i
    if dp[i][num] < minlen:
        minlen = dp[i][num]
        a, b = i, num
reslist = []
while a != 0 and b != 0:
    if a > b:
        reslist.append(1)
        a = checked[a][b]
    else:
        reslist.append(2)
        b = checked[a][b]
while a > 0:
    a -= 1
    reslist.append(1)
while b > 0:
    b -= 1
    reslist.append(2)
reslist.reverse()
print(minlen)
print(*reslist, sep="\n")