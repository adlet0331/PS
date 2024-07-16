import sys
input = sys.stdin.readline
# 10^5
data = list(map(int, input().split()))[:-1]
N = len(data)
INF = 10000000
# 그자리 1, 가운데서 2, 대각선 3, 반대 4
# dp 설계
# dp[i][l][r]
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(N)]
dp[0][data[0]][0] = 2
dp[0][0][data[0]] = 2

def cost(start, end):
    if start == 0:
        return 2
    elif start == end:
        return 1
    elif abs(start - end) % 2 == 0:
        return 4
    else:
        return 3
    
for i in range(1, N):
    for j in range(5):
        leftmincost = INF
        rightmincost = INF
        for k in range(5):
            leftmincost = min(leftmincost, dp[i-1][k][j] + cost(k, data[i]))
            rightmincost = min(leftmincost, dp[i-1][j][k] + cost(k, data[i]))
        dp[i][data[i]][j] = leftmincost
        dp[i][j][data[i]] = rightmincost
result = INF
for i in range(5):
    for j in range(5):
        result = min(dp[N-1][i][j], result)
print(result)