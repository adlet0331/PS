N = int(input())

dirlist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(N):
    [row, col, cnt] = list(map(int, input().split(" ")))
    datalist = [[0 for _ in range(col)] for _ in range(row)]
    for _ in range(cnt):
        [r, c] = list(map(int, input().split(" ")))
        datalist[r][c] = 1
    cnt = 0
    for r in range(row):
        for c in range(col):
            if datalist[r][c] == 1:
                cnt += 1
                datalist[r][c] = 0
                findqueue = []
                findqueue.append((r,c))
                while findqueue:
                    (qr, qc) = findqueue.pop()
                    for dir in dirlist:
                        if qr + dir[0] >= row or qr + dir[0] < 0 or qc + dir[1] >= col or qc + dir[1] < 0:
                            continue
                        if datalist[qr + dir[0]][qc + dir[1]] == 1:
                            datalist[qr + dir[0]][qc + dir[1]] = 0
                            findqueue.append((qr + dir[0], qc + dir[1]))
    print(cnt)