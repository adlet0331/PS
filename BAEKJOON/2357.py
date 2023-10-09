import sys
import math
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M = map(int, input().split())
numlist = [0]
for _ in range(N):
    numlist.append(int(input()))
rangelist = []
for _ in range(M):
    rangelist.append(list(map(int, input().split())))
min2square = 1 << (math.ceil(math.log2(N)) + 1)
segtree = [0 for _ in range(min2square)]

def makeseg(start, end, index):
    if start == end:
        segtree[index] = (numlist[start], numlist[start])
        return (numlist[start], numlist[start])
    mid = (start + end) // 2
    lchild = makeseg(start, mid, index * 2)
    rchild = makeseg(mid + 1, end, index * 2 + 1)
    segtree[index] = (min(lchild[0], rchild[0]), max(lchild[1], rchild[1]))
    return segtree[index]
makeseg(1, N, 1)

def findminmax(start, end, s, e, index):
    if s <= start and end <= e:
        return segtree[index]
    if e < start or end < s:
        return(10**9 + 1, 0)
    mid = (start + end) // 2
    lchild = findminmax(start, mid, s, e, index * 2)
    rchild = findminmax(mid + 1, end, s, e, index * 2 + 1)
    return (min(lchild[0], rchild[0]), max(lchild[1], rchild[1]))

for node in rangelist:
    answer = findminmax(1, N, node[0], node[1], 1)
    print(answer[0], answer[1])