import sys

# N: 학생수, K: 뽑을 인원, X: 두 능력치 합
N, K, X = map(int, sys.stdin.readline().split())
# (a, X-a)
students = []
for _ in range(N):
    a, _ = map(int, sys.stdin.readline().split())
    students.append(a)
# 항상 능력치는 (K * X - VAL) * VAL
# K * X // 2 와 가장 차이가 적은 K개로 이루어진 부분합 구하기 

# dp[i][j][k] index 0 ~ i인 학생만 썼을 때, j명을 썼을 때, 능력치 k에 도달할 수 있는가?
# 16000 * 80 * 80 = 102,400,000 < 512,000,000 B
TSUM = K * X
dp = [[[False for _ in range(TSUM + 1)] for _ in range(K + 1)] for _ in range(N)]
dp[0][0][0] = True
dp[0][1][students[0]] = True

for i in range(1, N):
    for j in range(min(i + 2, K + 1)):
        for finding_val in range(TSUM + 1):
            if dp[i-1][j][finding_val]:
                dp[i][j][finding_val] = True
            elif finding_val - students[i] >= 0 and j >= 1 and dp[i - 1][j - 1][finding_val - students[i]]:
                dp[i][j][finding_val] = True
VAL = 0
for i in range(N):
    for k in range(TSUM + 1):
        if dp[i][K][k] and k * (TSUM - k) > VAL * (TSUM - VAL):
            VAL = k
print(VAL * (TSUM - VAL))