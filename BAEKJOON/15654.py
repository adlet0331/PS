import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

def selnum(n, m):
    cnt = 1
    for i in range(n, n-m, -1):
        if i != 0:
            cnt *= i
    return cnt

results = [[] for _ in range(selnum(N, M))]
def make_seq(indexs, sindex, ccnt):
    global results
    for i in indexs:
        seqnum = selnum(len(indexs) - 1, ccnt-1)
        for index in range(sindex, sindex + seqnum):
            results[index].append(i)
        if ccnt > 1:
            newindexs = indexs.copy()
            newindexs.remove(i)
            make_seq(newindexs, sindex, ccnt - 1)
        sindex += seqnum

make_seq([i for i in range(N)], 0, M)
for res in results:
    resout = ""
    for i in res:
        resout += f"{data[i]} "
    sys.stdout.write(resout.strip() + "\n")