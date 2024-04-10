import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

acnt = len(A)
bcnt = len(B)
# dp[i][j] : A를 i까지, B를 j까지 포함 시켰을 때 최장 수열
# dp[i][j] = max(dp[i-1][j-1] + 1 if A[i] == B[j], dp[i][j-1], dp[i-1][j])

dp = [[0 for _ in range(acnt)] for _ in range(bcnt)]
dp[0][0] = 1 if A[0] == B[0] else 0
for i in range(1, bcnt):
    dp[i][0] = max(dp[i-1][0], 1 if B[i] == A[0] else 0)
for i in range(1, acnt):
    dp[0][i] = max(dp[0][i-1], 1 if B[0] == A[i] else 0)
for i in range(1, bcnt):
    for j in range(1, acnt):
        dp[i][j] = max(dp[i-1][j-1] + (1 if B[i] == A[j] else 0), dp[i][j-1], dp[i-1][j])
# print(dp)
print(dp[bcnt-1][acnt-1])