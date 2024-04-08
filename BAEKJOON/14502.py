from collections import deque

N, M = map(int, input().split())
mdata = []
virus_positions = []
empty_positions = []
for r in range(N):
    rlist = list(map(int, input().split()))
    for c in range(len(rlist)):
        if rlist[c] == 0:
            empty_positions.append((r, c))
        if rlist[c] == 2:
            virus_positions.append((r, c))
    mdata.append(rlist)

def get_safecnt(mmdata, virus_positions, pos1, pos2, pos3):
    visited = []
    for mlist in mmdata:
        newlist = []
        for mdata in mlist:
            newlist.append(mdata == 0)
        visited.append(newlist)
    visited[pos1[0]][pos1[1]] = False
    visited[pos2[0]][pos2[1]] = False
    visited[pos3[0]][pos3[1]] = False
    find_queue = deque(virus_positions)
    find_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while find_queue:
        (row, col) = find_queue.pop()
        visited[row][col] = False
        for (dr, dc) in find_directions:
            if row + dr >= N or row + dr < 0 or col + dc >= M or col + dc < 0:
                continue
            elif visited[row + dr][col + dc]:
                find_queue.append((row + dr, col + dc))
    cnt = 0
    for mlist in visited:
        for mdata in mlist:
            if mdata:
                cnt += 1
    return cnt

empty_cnt = len(empty_positions)
# N, M 최대값 8이고 벽은 딱 3개 무조건 세워야함. 전부 해보면 될듯
result = 0
for i in range(empty_cnt):
    for j in range(i+1, empty_cnt):
        for k in range(j+1, empty_cnt):
            result = max(result, get_safecnt(mdata, virus_positions, empty_positions[i], empty_positions[j], empty_positions[k]))
print(result)