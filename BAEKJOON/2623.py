from collections import deque

N, M = map(int, input().split())
p2cgraph = [[] for _ in range(N + 1)]
ranklist = [0 for _ in range(N + 1)]
for _ in range(M):
    dlist = list(map(int, input().split()))
    for i in range(1, dlist[0]):
        p2cgraph[dlist[i]].append(dlist[i+1])
        ranklist[dlist[i + 1]] += 1
findqueue = deque()
for i in range(1, N+1):
    if ranklist[i] == 0:
        findqueue.append(i)
result = []
while findqueue:
    node = findqueue.popleft()
    result.append(node)
    for child in p2cgraph[node]:
        ranklist[child] -= 1
        if ranklist[child] == 0:
            findqueue.append(child)
if len(result) != N:
    print(0)
else:
    print(*result, sep="\n")