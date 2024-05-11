N = int(input())
mdata = []
for _ in range(N):
    mdata.append(input())
def areacnt(N, mdata):
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                start = mdata[i][j]
                fqueue = [(i, j)]
                visited[i][j] = True
                while fqueue:
                    (ii, jj) = fqueue.pop()
                    for direction in directions:
                        ni, nj = ii + direction[0], jj + direction[1]
                        if ni < 0 or nj < 0 or ni >= N or nj >= N:
                            continue
                        if not visited[ni][nj] and start == mdata[ni][nj]:
                            fqueue.append((ni, nj))
                            visited[ni][nj] = True
    return cnt
new_mdata = []
for data in mdata:
    new_mdata.append(data.replace("R", "G"))
print(f"{areacnt(N, mdata)} {areacnt(N, new_mdata)}")