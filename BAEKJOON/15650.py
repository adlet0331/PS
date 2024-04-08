import sys

#  1 ~ N, 중복없이 M개를 고른 수열 모두 구하기
N, M = map(int, sys.stdin.readline().split())
def combination(n, m):
    cnt = 1
    for i in range(n, n-m, -1):
        cnt *= i
        cnt = cnt // (n - i + 1)
    return cnt

results = [[] for _ in range(combination(N, M))]
def make_seq(start, end, sindex, ccnt):
    global results
    for i in range(start, end - ccnt + 2):
        seqnum = combination(end - i, ccnt - 1)
        for index in range(sindex, sindex + seqnum):
            results[index].append(i)
        if ccnt > 1:
            make_seq(i + 1, end, sindex, ccnt - 1)
        sindex += seqnum
make_seq(1, N, 0, M)
for res in results:
    print(*res, sep = " ")