'''
정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)

Kruskal 알고리즘으로는 안됨 (ElogE 했는데 안됨)

--> union - find 알고리즘 제대로 안해놔서.

'''

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
nodearr = []
for _ in range(E):
    a, b, val = map(int, input().split())
    nodearr.append((a, b, val))

nodearr.sort(key=lambda x: x[2])
ufarr = [i for i in range(0, V + 1)]

def root(node):
    if node == ufarr[node]:
        return node
    ufarr[node] = root(ufarr[node])
    return ufarr[node]

def union_parent(a, b):
    a = root(a)
    b = root(b)

    if a < b:
        ufarr[a] = b
    else:
        ufarr[b] = a
    
cnt = 0
cval = 0
for [a, b, val] in nodearr:
    if root(a) != root(b):
        union_parent(a, b)
        cnt += 1
        cval += val
    if cnt == V-1:
        break
print(cval)

# 프림
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
linearr = [[] for _ in range(V + 1)]
for _ in range(E):
    [a, b, val] = list(map(int, input().split()))
    linearr[a].append((b, val))
    linearr[b].append((a, val))

ufarr = [i for i in range(0, V + 1)]
    
cnt = 0
cval = 0
connected_nodes = [1]
for _ in range(V - 1):
    all_lines = []
    for cnode in connected_nodes:
        for line in linearr[cnode]:
            if not line[0] in connected_nodes:
                all_lines.append(line)
    all_lines.sort(key=lambda x: x[1])
    nline = all_lines[0]
    cval += nline[1]
    connected_nodes.append(nline[0])
    
print(cval)