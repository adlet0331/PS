from collections import deque

def find_max_len_node(snode, tree):
    '''시간초과됨'''
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

N = int(input())
tree_list = [[] for _ in range(N + 1)]
for i in range(N):
    ilist = list(map(int, input().split()))
    index = ilist[0]
    for j in range((len(ilist) - 1) // 2):
        tree_list[index].append((ilist[j * 2 + 1], ilist[j*2 + 2]))
        tree_list[ilist[j * 2 + 1]].append((index, ilist[j*2 + 2]))

fresult = find_max_len_node(1, tree_list)
print(find_max_len_node(fresult[1], tree_list)[0])
