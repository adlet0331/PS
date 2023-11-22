'''
N, M 최대 10^5, 시간 제한 1.5초
O(n log(n)) 안에 해결해야함

DP 방식으로 해결 시도

11437은 됐는데 이건 안되네 왜 안된다냐 열심히 최적화 했는데

O(logN) 인 방법으로 시도해 보자

탐색을 할 때, 이전 건 O(N)인 방법이였음. 
부모 노드를 이진 탐색 마냥 O(log N) 으로 탐색하면 된다네 왜 될까

2 ^ i 인 노드들만 저장해서 탐색하면 이진 탐색과 같은 효능을 내는 듯. 
이해는 되지만 이걸 어떻게 발상으로 하지? 몰 루 많이 풀어보면 이렇게 시간 복잡도 줄이는 방법이 술술 나오는 경지가 되지 않을까..
'''
import sys
from collections import deque
from math import log2
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

# (depth, parentnodes)
tree = [-1 for _ in range(N + 1)]
tree[1] = (1, [0])
deq = deque()
deq.append(1)
# Make Tree, O(N * log N)
while deq:
    pnode = deq.popleft()
    (pdepth, gparentnodes) = tree[pnode]
    for childval in nodearr[pnode]:
        parentnodearr = [pnode]
        i = 0
        (_, find_parentnodes) = tree[pnode]
        # 처음 1은 그냥 넘어감
        # 2 ^ i 씩 넘어가면서 parentnodearrdp 2 ^ (i + 1) 번째 부모 추가
        # i 가 int(log2(pdepth)) 이하일 때 계속 실행 (depth가 2라면 i 가 0도 안함, depth가 3이면 딱 i가 0일때 까지)
        while i <= int(log2(pdepth)) - 1:
            next_pnode = find_parentnodes[i]
            (_, find_parentnodes) = tree[next_pnode]
            parentnodearr.append(next_pnode)
            i += 1

        tree[childval] = (pdepth + 1, parentnodearr)
        nodearr[childval].remove(pnode)
        deq.append(childval)
#print(str(tree) + '\n')
# M
for _ in range(M):
    anode, bnode = map(int, input().split())

    if tree[anode][0] < tree[bnode][0]:
        anode, bnode = bnode, anode
    # anode depth > bnode
    (adepth, aparentnodes) = tree[anode]
    (bdepth, bparentnodes) = tree[bnode]

    if adepth == 1 or bdepth == 1:
        print(str(1) + '\n')
        continue

    # up anode until adepth = bnode
    ai = 0
    #O(logN)
    while adepth != bdepth:
        if len(aparentnodes) <= ai:
            anode = aparentnodes[ai - 1]
            (adepth, aparentnodes) = tree[anode]
            ai = 0
        #print(str(aparentnodes))
        (adepth, _) = tree[aparentnodes[ai]]
        # 같으면 대입 후 while 탈출
        if adepth == bdepth:
            anode = aparentnodes[ai]
            (_, aparentnodes) = tree[anode]
            break
        # 너무 갔으면 그 이전으로 돌리고 최신화, 다시 탐색 시작
        elif adepth < bdepth:
            anode = aparentnodes[ai - 1]
            (adepth, aparentnodes) = tree[anode]
            ai = 0
            continue
        # 여전히 adepth가 작으면 다음으로
        else:
            ai += 1

    # 예외처리
    if anode == bnode:
        print(str(anode) + '\n')
        continue
    index = 0
    # anode, bnode 움직이면서 공통 조상 찾기 O(logN)
    while True:
        if len(aparentnodes) == index:
            (_, aparentnodes) = tree[aparentnodes[index - 1]]
            (_, bparentnodes) = tree[bparentnodes[index - 1]]
            index = 0

        # 첫번째, 혹은 두번째 부모가 처음으로 같을 때
        if aparentnodes[index] == bparentnodes[index] and index <= 1:
            print(str(aparentnodes[index]) + '\n')
            break
        # 부모가 같지만 좀 먼 부모(4번째 부터)가 같을 때 
        elif aparentnodes[index] == bparentnodes[index]:
            (_, aparentnodes) = tree[aparentnodes[index - 1]]
            (_, bparentnodes) = tree[bparentnodes[index - 1]]
            index = 0
        # 다르면 탐색 계속
        else:
            index += 1