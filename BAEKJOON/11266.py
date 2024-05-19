import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# start 에서 시작해서 순회
spanning_tree = [0 for _ in range(V + 1)]
result = set()
scnt = 1
def dfs(node, isroot):
    global scnt
    spanning_tree[node] = scnt
    scnt += 1

    currscnt = spanning_tree[node]
    childcnt = 0
    for child in graph[node]:
        if spanning_tree[child]:
            currscnt = min(currscnt, spanning_tree[child])
            continue
        
        childcnt += 1
        childnum = dfs(child, False)
        
        # child중 하나라도 지금 node 이전 노드에 도달 안되면 result
        if not isroot and childnum >= spanning_tree[node]:
            result.add(node)

        currscnt = min(childnum, currscnt)

    if isroot and childcnt >= 2:
        result.add(node)

    return currscnt

for i in range(1, V+1):
    if not spanning_tree[i]:
        dfs(i, True)
print(spanning_tree)
result = sorted(list(result))
print(len(result))
print(*result, sep=" ")