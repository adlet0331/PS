import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
requests = []
for _ in range(N):
    requests.append(list(map(int, input().split(" "))))
# 데이터 - 1: 빼기, 2: 넣기 / 빼기면 순위, 넣기면 맛의 정도 / 개수

# 세그먼트 트리
#
seg_tree = [-1 for _ in range(4000001)]

def update(num, diff):
    index = 1
    while True:
        seg_tree[index][0] += diff
        if seg_tree[index][1] == seg_tree[index][2] == num:
            return
        [_, rmin, _] = seg_tree[index * 2 + 1]
        if rmin > num:
            index *= 2
        else:
            index = index * 2 + 1

def findwithrank(rank):
    index = 1
    while True:
        [_, min, max] = seg_tree[index]
        if min == max:
            return min
        else:
            [lcnt, _, _] = seg_tree[index * 2]
            if lcnt >= rank:
                index *= 2
            else:
                rank -= lcnt
                index = index * 2 + 1

# Init seg tree
index = 1
def makesegtree(index, min, max):
    seg_tree[index] = [0, min, max]
    if min != max:
        mid = (min + max) // 2
        makesegtree(index * 2, min, mid)
        makesegtree(index * 2 + 1, mid + 1, max)
    return
makesegtree(1, 1, 1000000)

for req in requests:
    # 순위로 빼기 
    if req[0] == 1:
        result = findwithrank(req[1])
        update(result, -1)
        print(f"{result}\n")
    # 넣기 혹은 더하기
    elif req[0] == 2:
        update(req[1], req[2])