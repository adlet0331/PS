from collections import deque

N = int(input())
tree_list = [[] for _ in range(N + 1)]
for i in range(N):
    ilist = list(map(int, input().split()))
    index = ilist[0]
    for j in range(len(ilist) // 2 - 1):
        tree_list[index].append((ilist[j * 2 + 1], ilist[j * 2 + 2]))

def find_longest_len_and_node(snode):
    len_list = [-1 for _ in range(len(tree_list))]
    len_list[snode] = 0
    snodes = deque()
    snodes.append(snode)
    while len(snodes) != 0:
        snode = snodes.popleft()
        for node_data in tree_list[snode]:
            tnode = node_data[0]
            #print("snode, tnode : ", snode, tnode)
            if len_list[tnode] != -1:
                continue
            len_list[tnode] = len_list[snode] + node_data[1]
            for tnode_data in tree_list[tnode]:
                new_tnode = tnode_data[0]
                if len_list[new_tnode] == -1:
                    snodes.append(new_tnode)
                    len_list[new_tnode] = len_list[tnode] + tnode_data[1]
                    #print("appended: ", new_tnode, len_list)
    max_result = (-1, 0)
    for len_node in range(len(len_list)):
        if max_result[1] < len_list[len_node]:
            max_result = (len_node, len_list[len_node])
    #print(max_result, len_list)
    return max_result

print(find_longest_len_and_node(find_longest_len_and_node(1)[0])[1])