"""
dp로 잘 해결함!

나는 골5딱인건가
"""


T, W = map(int, input().split(" "))
datalist = [list(), list()]
curr_index = num = int(input())
cnt = 1
for _ in range(T - 1):
    num = int(input())
    if num == curr_index:
        cnt += 1
    else:
        datalist[curr_index-1].append(cnt)
        datalist[2-curr_index].append(0)
        cnt = 1
        curr_index = num
datalist[curr_index-1].append(cnt)
datalist[2-curr_index].append(0)

def get_max(datalist, max_move):
    dlen = len(datalist[0])
    # 2차원 배열
    # 1, 2 어디에 있는지 저장 안해도 됨 
    dp = [[0 for _ in range(dlen)] for _ in range(max_move + 1)]

    #초기화
    dp[0][0] = datalist[0][0]
    dp[1][0] = datalist[1][0]
    for i in range(1, dlen):
        dp[0][i] = dp[0][i-1] + datalist[0][i]
    for move in range(1, max_move + 1):
        dp[move][0] = datalist[1][0]

    for mcnt in range(1, max_move+1):
        for i in range(1, dlen):
            staycnt = dp[mcnt][i-1] + datalist[mcnt % 2][i]
            movecnt = dp[mcnt-1][i-1] + datalist[mcnt % 2][i]
            maxcnt = movecnt if movecnt > staycnt else staycnt
            dp[mcnt][i] = maxcnt

    maxresult = 0
    for dplist in dp:
        if maxresult < dplist[dlen - 1]:
            maxresult = dplist[dlen - 1]
    
    return maxresult

print(get_max(datalist, W))