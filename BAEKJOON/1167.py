from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
for i in range(N):
    ilist = list(map(int, input().split()))
    index = ilist[0]
    for j in range((len(ilist) - 1) // 2):
        tree[index].append((ilist[j * 2 + 1], ilist[j*2 + 2]))
        tree[ilist[j * 2 + 1]].append((index, ilist[j*2 + 2]))


# 시간 초과..
def find_max_len_node(snode, tree):
    fqueue = deque()
    fqueue = [(snode, -1, 0)]
    maxlen = 0
    maxnode = 0
    while fqueue:
        data = fqueue.pop()
        cnode = data[0]
        fnode = data[1]
        length = data[2]
        eflag = True
        for ldata in tree[cnode]:
            if ldata[0] == fnode:
                continue
            fqueue.append((ldata[0], cnode, length + ldata[1]))
            eflag = False
        if eflag and maxlen < length:
            maxlen = length
            maxnode = cnode
    return (maxlen, maxnode)

fresult = find_max_len_node(1, tree)
print(find_max_len_node(fresult[1], tree)[0])