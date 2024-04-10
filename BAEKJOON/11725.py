import sys
input = sys.stdin.readline
N = int(input())
treedata = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    treedata[a].append(b)
    treedata[b].append(a)
parents = [0 for _ in range(N+1)]
find_queue = [1]
while find_queue:
    cpar = find_queue.pop()
    for child in treedata[cpar]:
        if parents[child] == 0:
            parents[child] = cpar
            find_queue.append(child)
for i in range(2, N+1):
    print(parents[i])