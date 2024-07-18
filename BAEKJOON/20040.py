import sys
input = sys.stdin.readline
# N = 5*10^5, M=10^6
N, M = map(int, input().split())
data = []
for _ in range(M):
    a, b = map(int, input().split())
    data.append((a, b))

# 각 노드는 루트를 가지고 있음, 연결된 노드 중 가장 작은 노드 수를 루트로 가짐.
# 연결 되려는 두 노드의 루트가 같으면 사이클 생성되는거임, 아니면 갱신
parent = [i for i in range(N)]
uniongroup = {}
result = 1
for (anode, bnode) in data:
    if parent[anode] > parent[bnode]:
        anode, bnode = bnode, anode
    aparent, bparent = parent[anode], parent[bnode]
    if aparent == bparent:
        print(result)
        break
    else:
        if aparent not in uniongroup:
            uniongroup[anode] = [anode]
        for bnnode in uniongroup[bparent] if bparent in uniongroup else [bnode]:
            uniongroup[aparent].append(bnnode)
            parent[bnnode] = aparent
    result += 1
if result == M + 1:
    print(0)