import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    N = int(input())
    sdata = []
    for _ in range(2):
        sdata.append(list(map(int, input().split())))
    # dp[i][j][0] i열 j행까지 했을 때 최대 점수. 0은 해당 칸 사용 X, 1은 사용 O
    dp = [[[0, 0] for _ in range(N)] for _ in range(2)]
    for j in range(N):
        for i in range(2):
            dp[i][j][0] = max(dp[i][j-1 if j > 0 else 0][0], dp[i][j-1 if j > 0 else 0][1])
        for i in range(2):
            dp[i][j][1] = max(dp[1-i][j][0], dp[i][j-1 if j > 0 else 0][0]) + sdata[i][j]
    print(max(dp[0][N-1][0], dp[0][N-1][1], dp[1][N-1][0], dp[1][N-1][1]))