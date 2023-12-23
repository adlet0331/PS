import sys
input = sys.stdin.readline

# Bubble Sort을 하면 얼마나 떨어져 있는지 세기
# N <= 500,000  N^2 = 2 * 10 ^ 11 안됨, O(N logN) 안에 해결해야함

# 버블 소트, 순서 상관없이 정해진 교환을 하면 되나?
# 답은 No 왜?
# 한 곳이 여러번 바뀌기 때문에, 정해진 순서대로 해야함.
# 0 ~ N-1, 0 ~ N-2, ... 0 이렇게 해야 함.
# 교환 할 필요 없으면 안하고, 필요하면 하고

# 아이디어 1
# 정렬 후, 각 요소 떨어져 있는 거리의 합 / 2
# 1. 중복되는 요소는 어떻게 처리? - 어떻게든 되지 않을까

# 찾아보고 안 아이디어 2
# 자기보다 앞에 있는, 작은 아이들 수 만큼 이동함
# 이 개수를 세면 된다!

# 그냥 세면 어떻게 되냐.. O(N^2) 가 되어버림
# 그러므로 세그먼트 트리로 해야한다! 정렬해서 작은 수 부터 세그먼트 트리에 작은 수의 index에 1로써 넣도록 하자
# 이렇게 넣으면, 넣인 요소는 지금 넣는 요소들 보다 항상 작음 그래서 지금 넣는 요소 이상의 index에 있는 애들을 부분합으로 세어서 cnt에 더해주면 됨. 
# + 이슈가 하나 더있음. 요소가 10^9 이하라 압축을 해야함.
# 어떻게 할거냐, 그냥 크기 순으로 1 ~ 50만으로 하면 될듯?


N = int(input())
data = list(map(int, input().split()))
# 인덱스랑 데이터
IandDlist = [[i, data[i]] for i in range(N)]
# 데이터의 크기대로 정렬
IandDlist = sorted(IandDlist, key = lambda x: x[1])
# [0, -10, 5, -5, 10]
# [[1, -10], [3, -5], [0, 0], [2, 5], [4, 10]]

seg_tree = [0 for _ in range(N * 4)]

def getval_seg(start, end, node, sindex, eindex):
    if sindex > end or eindex < start:
        return 0
    if sindex <= start and end <= eindex:
        return seg_tree[node]
    mid = (start + end) // 2
    left = getval_seg(start, mid, node * 2, sindex, eindex)
    right = getval_seg(mid + 1, end, node * 2 + 1, sindex, eindex)
    return  left + right 

def update_seg(start, end, node, index):
    if start == end:
        seg_tree[node] = 1
        return
    if index < start or index > end:
        return
    mid = (start + end) // 2
    if index <= mid:
        update_seg(start, mid, node * 2, index)
    else:
        update_seg(mid + 1, end, node * 2 + 1, index)
    seg_tree[node] = seg_tree[node * 2] + seg_tree[node * 2 + 1]

# 하나씩 넣어서 node 업데이트
cnt = 0
for [index, val] in IandDlist:
    update_seg(0, N-1, 1, index)
    cnt += getval_seg(0, N-1, 1, index + 1, N-1)

print(cnt)