import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().strip().split())))
sum_list = [[0 for _ in range(N+1)] for _ in range(N+1)]
for r in range(1, N+1):
    cnt = 0
    for c in range(1, N+1):
        cnt += data[r-1][c-1]
        sum_list[r][c] = sum_list[r-1][c] + cnt
for _ in range(M):
    y, x, yy, xx = map(int, input().strip().split())
    cnt = sum_list[yy][xx] - sum_list[y-1][xx] - sum_list[yy][x-1] + sum_list[y-1][x-1]
    print(cnt)