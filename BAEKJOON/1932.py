N = int(input())
tadata = []
dp = []
for _ in range(N):
    slist = list(map(int, input().split()))
    tadata.append(slist)
    dp.append([0 for _ in slist])
dp[0][0] = tadata[0][0]
for floor in range(1, N):
    for i in range(floor + 1):
        dp[floor][i] = max(dp[floor-1][i] if i != floor else 0, dp[floor-1][i-1] if i > 0 else 0) + tadata[floor][i]
result = 0
for res in dp[N-1]:
    result = max(res, result)
print(result)