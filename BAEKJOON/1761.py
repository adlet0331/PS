# N: 40000, M: 10000
# 트리, 최소 공통 조상 찾기
# O(M * N)
import math, sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
graph = [[] for _ in range(N + 1)]
rank = [-1 for _ in range(N + 1)]
c2p = [[] for _ in range(N + 1)]
c2plen = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
root = 0
for i in range(1, N + 1):
    if len(graph[i]) >= 2:
        root = i
        break
# Build tree
rank[root] = 0
bqueue = deque()
bqueue.append((root, 0))
while bqueue:
    (parent, rnum) = bqueue.popleft()
    for (child, length) in graph[parent]:
        if rank[child] >= 0:
            continue
        bqueue.append((child, rnum + 1))
        rank[child] = rnum + 1
        c2p[child].append(parent)
        c2plen[child].append(length)
        # c2p, c2plen 채우기. 지금 child의 parent들은 모두 채워져 있음
        clen = length
        i = 0
        nparent = parent
        while i <= math.log2(rnum + 1) - 1:
            # print(f"{i}, {child}, {nparent}, {c2p[nparent]}, {c2plen[nparent]}\n")
            clen += c2plen[nparent][i]
            nparent = c2p[nparent][i]
            c2p[child].append(nparent)
            c2plen[child].append(clen)
            i += 1
# print(f"{c2p}\n {c2plen}\n{rank}\n")
# O(N^2) 여기가 문제다.. 위에 트리 만들면서 하도록 개선
# for i in range(1, N+1):
#     crank = rank[i]
#     if crank < 4:
#         continue
#     cindex = 1
#     cparent = c2p[i][0]
#     while crank > 2 ** cindex:
#         l = 0
#         for _ in range(2 ** (cindex - 1)):
#             l += graph[cparent][c2p[cparent][0]]
#             cparent = c2p[cparent][0]
#         c2p[i].append(cparent)
#         c2plen[i].append(l)
#         cindex += 1

def jumpcntparent(a, cnt):
    l = 0
    while cnt > 0:
        jumpindex = int(math.floor(math.log2(cnt)))
        # print(f"{jumpindex}, {c2p[a]}\n")
        l += c2plen[a][jumpindex]
        a = c2p[a][jumpindex]
        cnt -= 2 ** jumpindex
    return a, l

def getdistance(a, b):
    result = 0
    while a != b:
        i = 0
        while i < len(c2p[a]) - 1:
            if c2p[a][i] == c2p[b][i]:
                break
            i += 1
        i = max(0, i - 1)
        result += c2plen[a][i] + c2plen[b][i]
        a, b = c2p[a][i], c2p[b][i]
    return result

for _ in range(int(input())):
    a, b = map(int, input().split())
    arank, brank = rank[a], rank[b]
    result = 0
    if arank != brank:
        if arank < brank:
            a, b = b, a
        # O(log(N))
        newaparent, l = jumpcntparent(a, abs(arank - brank))
        result += l
        a = newaparent
    # O(log(N))
    result += getdistance(a, b)
    print(f"{result}\n")