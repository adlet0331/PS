N, K = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
dp = [0 for _ in range(K + 1)]

# O(N * K)
for weight, value in data:
    if weight > K:
        continue
    for i in range(K, weight, -1):
        if dp[i - weight] == 0:
            continue
        dp[i] = max(dp[i - weight] + value, dp[i])
    dp[weight] = max(dp[weight], value)
result = 0
for res in dp:
    result = max(result, res)
print(result)