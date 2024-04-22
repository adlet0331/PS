N, M = map(int, input().split())
mdata = list(map(int, input().split()))
cdata = list(map(int, input().split()))
# M = 10,000,000 N = 100
# dp[c] 코스트 c를 사용 했을 때 최대 메모리
dp = [0 for _ in range(10001)]
for i in range(N):
    memory = mdata[i]
    cost = cdata[i]
    for c in range(10001 - cost - 1, -1, -1):
        if dp[c] + memory > dp[c + cost]:
            dp[c + cost] = dp[c] + memory
for i in range(10001):
    if dp[i] >= M:
        print(i)
        break