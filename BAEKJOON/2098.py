# N = 16
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
# dp[i:  현재위치][visited: 비트마스크]
# dp[i][2 ** i] : i에서 시작해서 다 돈 것의 최소 경로 값    
dp = [[-1 for _ in range(2 ** N)] for _ in range(N)]
def dfs(cpos, bitmask):
    global dp
    if bitmask == (1 << N) - 1:
        if graph[cpos][0] == 0:
            return 100000000
        else:
            return graph[cpos][0]
    cnt = 100000000
    for next in range(N):
        if (bitmask & (1 << next)) or graph[cpos][next] == 0:
            continue
        nbitmask = bitmask | (1 << next)
        res = (dfs(next, nbitmask) if dp[next][nbitmask] == -1 else dp[next][nbitmask]) + graph[cpos][next]
        cnt = min(res, cnt)
    dp[cpos][bitmask] = cnt
    return cnt
print(dfs(0, 1))