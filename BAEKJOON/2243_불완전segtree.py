import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
requests = []
for _ in range(N):
    requests.append(list(map(int, input().split(" "))))
# 데이터 - 1: 빼기, 2: 넣기 / 빼기면 순위, 넣기면 맛의 정도 / 개수

# 세그먼트 트리
# 1. leaf가 아닌 노드들이 가지고 있는 것
#    최대 최소 순위, 최대 최소 값
    
# 넣고 빼기 함수로 구현 O(logn)
# 탐색 기준: 자식 2개 비교, 최대 최소 값 보고 넣기
seg_tree = [-1 for _ in range(4000001)]

# num이 음수면 빼기, 양수면 넣기
def putorget(val, num):
    index = 1
    # 넣기
    while num > 0:
        #print(f"{index}, {seg_tree[index]}\n")
        # 가장 처음 넣는 경우
        if index == 1 and seg_tree[index] == -1:
            seg_tree[index] = [num, val, val]
            return
        # 아닌 경우, 판별해서 만들어 가기
        else:
            [cnt, minval, maxval] = seg_tree[index]
            needtomakeleaf = -1
            # 끝인데 leaf 만들어야 하는 경우
            if minval == maxval and minval != val:
                needtomakeleaf = val
            # minval, maxval 업데이트
            if minval > val:
                minval = val
            elif maxval < val:
                maxval = val
            cnt += num
            seg_tree[index] = [cnt, minval, maxval]
            # 원래 leaf 노드였을 경우, 아래에 추가 아니면 넘어가기
            if needtomakeleaf != -1:
                # 추가된게 원래 값보다 작은 경우
                if needtomakeleaf == minval:
                    seg_tree[index * 2] = [num, needtomakeleaf, needtomakeleaf]
                    seg_tree[index * 2 + 1] = [cnt - num, maxval, maxval]
                elif needtomakeleaf == maxval:
                    seg_tree[index * 2] = [cnt - num, minval, minval]
                    seg_tree[index * 2 + 1] = [num, needtomakeleaf, needtomakeleaf]
                return
            elif minval == maxval and minval == val:
                return 
            # leaf 노드가 아닌 경우, 판별해서 index 변경
            # 개수가 적은 쪽으로 추가
            else:
                [lcnt, _, lmaxval] = seg_tree[index * 2]
                [rcnt, rminval, _] = seg_tree[index * 2 + 1]                
                if val < rminval:
                    index =  index * 2
                elif lmaxval < val and val < rminval:
                    if lcnt < rcnt:
                        index = index * 2
                    else:
                        index = index * 2 + 1
                else:
                    index =  index * 2 + 1
    # 빼기
    while num < 0:
        [cnt, minval, maxval] = seg_tree[index]
        # 해당 val의 leaf 노드까지 안착
        if minval == maxval:
            cnt += num
            seg_tree[index] = [cnt, minval, maxval]
            return
        # 아직 parent 노드 일때
        else:
            cnt += num
            [_, _, lmaxval] = seg_tree[index * 2]
            seg_tree[index] = [cnt, minval, maxval]
            if val <= lmaxval:
                index = index * 2
            else:
                index = index * 2 + 1

def get(rank):
    # print(str(seg_tree))
    index = 1
    while True:
        [cnt, minval, maxval] = seg_tree[index]
        cnt -= 1
        seg_tree[index][0] = cnt
        # leaf node인 경우
        if minval == maxval:
            return str(minval) + "\n"
        # leaf 노드가 아니면 이분탐색 진행
        else:
            [lcnt, _, _] = seg_tree[index * 2]
            if lcnt >= rank:
                index = index * 2
            else:
                rank -= lcnt
                index = index * 2 + 1

for req in requests:
    #print(str(seg_tree) + "\n")
    if req[0] == 1:
        print(get(req[1]))
    elif req[0] == 2:
        putorget(req[1], req[2])