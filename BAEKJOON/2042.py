N, M, K = map(int, input().split())
num_list = [0]
for i in range(N):
    num_list.append(int(input()))
min_2square = 1
while min_2square < N:
    min_2square *= 2
seg_tree = [0 for _ in range(min_2square * 2 + 1)]

def init_segment_tree(start, end, node):
    if start == end:
        seg_tree[node] = num_list[start]
        return seg_tree[node]
    mid = (start + end) // 2
    seg_tree[node] = init_segment_tree(start, mid, node * 2) + init_segment_tree(mid + 1, end, node * 2 + 1)
    return seg_tree[node]
init_segment_tree(1, N, 1)

cs_list = []
for index in range(M + K):
    isChange, num1, num2 = map(int, input().split())
    cs_list.append((isChange == 1, num1, num2))

def update_seg(start, end, node, index, diff):
    if index < start or end < index:
        return
    seg_tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update_seg(start, mid, node * 2, index, diff)
    update_seg(mid + 1, end, node * 2 + 1, index, diff)

def return_sum(start, end, node, left, right):
    if end < left or right < start:
        return 0
    elif left <= start and end <= right:
        return seg_tree[node]
    else:
        mid = (start + end) // 2
        return return_sum(start, mid, node * 2, left, right) + return_sum(mid + 1, end, node * 2 + 1, left, right)

for csnode in cs_list:
    (isChange, num1, num2) = csnode
    if isChange:
        update_seg(1, N, 1, num1, num2 - num_list[num1])
        num_list[num1] = num2
    else:
        print(return_sum(1, N, 1, num1, num2))