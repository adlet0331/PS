from collections import deque

col, row = map(int, input().split(" "))

tmap = [[] for _ in range(row + 2)]
tcnt = 0

for r in range(row + 2):
    if r == 0 or r == row + 1:
        for c in range(col + 2):
            tmap[r].append(-1)
        continue
    tmap[r].append(-1)
    for el in map(int, input().split()):
        tmap[r].append(el)
        tcnt += 1 if el != -1 else 0
    tmap[r].append(-1)

squeue = deque()
for r in range(row):
    for c in range(col):
        if tmap[1 + r][1 + c] == 1:
            squeue.append((r,c, 0))

day = 0
dirlist = [(0,1), (1,0), (-1,0), (0, -1)]
#print(tmap)
while squeue:
    tinfo = squeue.popleft()
    tcnt -= 1
    for dir in dirlist:
        if tmap[1 + tinfo[0] + dir[0]][1 + tinfo[1] + dir[1]] == 0:
            squeue.append((tinfo[0] + dir[0], tinfo[1] + dir[1], tinfo[2] + 1))
            tmap[1 + tinfo[0] + dir[0]][1 + tinfo[1] + dir[1]] = 1
    day = day if day > tinfo[2] else tinfo[2]

if tcnt == 0:
    print(day)
else:
    print(-1)