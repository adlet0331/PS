import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
# 걍 완전탐색하면 될듯
mincnt = 10000000
minnode = 101
for cnode in range(1, N+1):
    fnum = 0
    cnt = 0
    flist = [cnode]
    cntlist = [-1 for _ in range(N + 1)]
    # bfs로 탐색
    while len(flist) > 0:
        new_flist = []
        for fnode in flist:
            cntlist[fnode] = fnum
            cnt += fnum
            for friendnode in tree[fnode]:
                if cntlist[friendnode] == -1 and friendnode not in flist + new_flist:
                    new_flist.append(friendnode)
        flist = new_flist
        fnum += 1
    #print(f"{cnode} : {cnt}, {cntlist}")
    if mincnt > cnt:
        mincnt = cnt
        minnode = cnode
print(minnode)