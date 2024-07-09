import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
dp = [(data[i], data[i]) for i in range(3)] 
for i in range(1, N):
    data = list(map(int, input().split()))
    dp = [(min(dp[0][0], dp[1][0]) + data[0], max(dp[0][1], dp[1][1])+ data[0]), 
          (min(dp[0][0], dp[1][0], dp[2][0]) + data[1], max(dp[0][1], dp[1][1], dp[2][1]) + data[1]), 
          (min(dp[1][0], dp[2][0]) + data[2], max(dp[1][1], dp[2][1])+ data[2])]
print(f"{max(dp[0][1], dp[1][1] ,dp[2][1])} {min(dp[0][0], dp[1][0] ,dp[2][0])}")