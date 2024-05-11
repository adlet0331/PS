N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
result = 0
directions = [(-1, 0), (1, 0), (0, 1)]
for i in range(N):
    for j in range(M):
        findqueue = []
        if j < M - 1:
            findqueue.append([(i, j + 1)])
        if i < N - 1:
            findqueue.append([(i + 1, j)])
        if i > 0:
            findqueue.append([(i - 1, j)])
        for _ in range(2):
            new_findqueue = []
            for clist in findqueue:
                for cnode in clist:
                    for direction in directions:
                        ni, nj = cnode[0] + direction[0], cnode[1] + direction[1]
                        if (ni, nj) not in clist and ni >= 0 and nj >= 0 and ni < N and nj < M and not (ni == i and nj == j):
                            new_findqueue.append(clist + [(ni, nj)])
            findqueue = new_findqueue
        # print(i, j, findqueue)
        for clist in findqueue:
            cnt = data[i][j]
            for (ii, jj) in clist:
                cnt += data[ii][jj]
            result = max(cnt, result)
print(result)