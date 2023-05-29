N = int(input())
K = int(input())

def solve(tnum, snum):
    # dp [선택 개수][총 개수]
    dp = [[0 for _ in range(tnum + 1)] for _ in range(snum + 1)]
    divideas = 1000000003

    for total_num in range(1, tnum + 1):
        dp[0][total_num] = 1
        dp[1][total_num] = total_num

    for select_num in range(2, snum + 1):
        for total_num in range(2, tnum + 1):
            if select_num > total_num / 2:
                dp[select_num][total_num] = 0
            else:
                dp[select_num][total_num] = (dp[select_num][total_num - 1] + dp[select_num - 1][total_num - 2]) % divideas
    return dp[snum][tnum] % divideas

print(solve(N, K))