'''
N, M 최대 10^5, 시간 제한 1.5초
O(n log(n)) 안에 해결해야함

DP 방식으로 해결 시도

11437은 됐는데 이건 안되네 왜 안된다냐 열심히 최적화 했는데
'''
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nodearr = [[] for _ in range(N+1)]
# 메모리 N * 2 + 알파 사용
for _ in range(N - 1):
    [anode, bnode] = list(map(int, input().split()))
    nodearr[anode].append(bnode)
    nodearr[bnode].append(anode)
M = int(input())
questionarr = []
for _ in range(M):
    questionarr.append(list(map(int, input().split())))

# (depth, parentnode)
tree = [[] for _ in range(N + 1)]
tree[1] = (0, -1, 1)
deq = deque()
deq.append(1)
# Make Tree, O(N * log N)
while deq:
    pnode = deq.popleft()
    for childnode in nodearr[pnode]:
        tree[childnode] = (tree[pnode][0] + 1, pnode, childnode)
        nodearr[childnode].remove(pnode)
        deq.append(childnode)

answerarr = []
# Solve, O(MlogN)
for qnode in questionarr:
    [anode, bnode] = qnode
    if tree[anode][0] < tree[bnode][0]:
        anode, bnode = bnode, anode 
    (adepth, aparent, anode) = tree[anode]
    (bdepth, bparent, bnode) = tree[bnode]
    while adepth > bdepth:
        (adepth, aparent, anode) = tree[aparent]
    if anode == bnode:
        print(str(anode) + '\n')
        continue
    while adepth > 0:
        if aparent == bparent:
            print(str(aparent) + '\n')
            break
        (adepth, aparent, anode) = tree[aparent]
        (bdepth, bparent, bnode) = tree[bparent]