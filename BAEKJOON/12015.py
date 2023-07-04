N = int(input())
data = map(int, input().split())

dp = [0 for _ in range(N)]

def recurse(start):
    if dp[start] != 0:
        return dp[start]
    cnt = 1
    for i in range(start + 1, N):
        if data[start] < data[i]:
            cnt = max(cnt, recurse(i) + 1)
    dp[start] = cnt
    return cnt


mcnt = 0
for i in range(N):
    if dp[i] != 0:
        continue
    mcnt = max(mcnt, recurse(i))