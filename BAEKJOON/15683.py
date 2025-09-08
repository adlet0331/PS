N, M = map(int, input().split())
mincnt = N * M
mlist = []
cctv_list = [] # (cctv 번호, (row, col)) 최대: O(N) * 8 * 4^8, 2^19 = 10^6 굉장히 널럴하다
for row in range(N):
    rlist = list(map(int, input().split()))
    for col in range(M):
        if rlist[col] == 0 or rlist[col] == 6:
            if rlist[col] == 6:
                mincnt -= 1
            continue
        cctv_list.append((rlist[col], (row, col)))
        rlist[col] = 0
    mlist.append(rlist)
# mlist: 맵 구조
num_list = [0, 4, 2, 4, 4, 1]
cctv_dict = {
    1 : [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
    2 : [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
    3 : [[(0, 1), (1, 0)], [(0, 1), (-1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]],
    4 : [[(0, 1), (-1, 0), (0, -1)], [(1, 0), (-1, 0), (0, -1)], [(1, 0), (0, 1), (0, -1)], [(1, 0), (0, 1), (-1, 0)]],
    5 : [[(1, 0), (0, 1), (-1, 0), (0, -1)]]
}
cctv_rotate_list = []
total_rotate_cnt = 1
for cctv_num, _ in cctv_list:
    cctv_rotate_list.append(num_list[cctv_num])
    total_rotate_cnt *= num_list[cctv_num]


cnt = 0
result = 0
while cnt < total_rotate_cnt:
    view_cnt = 0
    newlist = [a[:] for a in mlist]
    index_list = []
    ncnt = cnt
    for i in cctv_rotate_list:
        index_list.append(ncnt % i)
        ncnt = ncnt // i

    for i, (num, (row, col)) in enumerate(cctv_list):
        for (rdir, cdir) in cctv_dict[num][index_list[i]]:
            nrow, ncol = row, col
            while nrow >= 0 and nrow < N and ncol >= 0 and ncol < M:
                if newlist[nrow][ncol] == 6:
                    break
                if newlist[nrow][ncol] == 0:
                    newlist[nrow][ncol] = 1
                    view_cnt += 1
                nrow += rdir
                ncol += cdir
    result = max(result, view_cnt)
    cnt += 1
print(mincnt - result)