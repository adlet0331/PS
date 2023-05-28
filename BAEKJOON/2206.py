"""
bfs로 해결

2차원 배열로 하려고 했더만, 부수었는지, 안 부수었는지
해야 해서 3차원으로 해야 함

최단거리로 잘 쳐내면 된다. 2차원으로 해서 삽질 많이 했당.

"""
from collections import deque

row, column = map(int, input().split(" "))
mmap = list()
for r in range(row):
    d = input()
    mmap_list = list()
    for i in d:
        mmap_list.append(i == "0")
    mmap.append(mmap_list)
# 0,0 to row-1, column-1
moves = [(-1,0), (0,-1), (0, 1), (1,0)]
dp = [[[0, 0] for _ in range(column)] for _ in range(row)]
def solve(startrow, startcol):
    queue = deque()
    queue.append((startrow, startcol, False, (1,0)))
    dp[0][0][0] = 1
    while queue:
        data = queue.popleft()
        cnt = dp[data[0]][data[1]][1 if data[2] else 0]
        if data[0] == row - 1 and data[1] == column - 1:
            return cnt
        for move in moves:
            # 왔던 방향 제외
            if move == (data[3][0] * (-1), data[3][1] * (-1)):
                continue
            
            r = data[0] + move[0]
            c = data[1] + move[1]

            # 맵 바깥 제외
            if r < 0 or c < 0 or r >= row or c >= column:
                continue
            # 벽 못 뚫을 상황에 벽으로 가는 경우 제외
            if not mmap[r][c] and data[2]:
                continue
            
            # 경우의 수 처리
            if mmap[r][c]:
                if 0 < dp[r][c][1 if data[2] else 0] and dp[r][c][1 if data[2] else 0] <= cnt + 1:
                    continue
                queue.append((r, c, data[2], move))
                dp[r][c][1 if data[2] else 0] = cnt + 1
            elif not mmap[r][c]:
                if 0 < dp[r][c][1] and dp[r][c][1] <= cnt + 1:
                    continue
                if data[2]:
                    continue
                dp[r][c][1] = cnt + 1
                queue.append((r, c, True, move))
    return -1
print(solve(0, 0))