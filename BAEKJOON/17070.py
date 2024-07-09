N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# [가로, 대각선, 세로]
dp[0][1][0] = 1
startr = 0
startc = 2
nowr = 1
nowc = 2

def filldp(row, col):
    if data[row][col] == 1:
        return
    dp[row][col][0] = dp[row][col - 1][0] + dp[row][col - 1][1]
    if data[row-1][col] == 0 and data[row][col-1] == 0:
        dp[row][col][1] = dp[row - 1][col - 1][0] + dp[row - 1][col - 1][1] + dp[row - 1][col - 1][2]
    dp[row][col][2] = dp[row - 1][col][1] + dp[row - 1][col][2]

while nowr < N or nowc < N:
    for c in range(startc, nowc):
        filldp(nowr, c)
    if nowc < N:
        for r in range(startr, nowr):
            filldp(r, nowc)
        filldp(nowr, nowc)
    nowc, nowr = nowc + 1, nowr + 1
print(sum(dp[N-1][N-1]))