N, M = map(int, input().split())
data = [0 for _ in range(107)]
for _ in range(N + M):
    start, end = map(int, input().split())
    data[start] = end
findqueue = [1]
visited = [False for _ in range(107)]
cnt = 0
while True:
    cnt += 1
    newqueue = []
    for node in findqueue:
        for i in range(1, 7):
            if data[node + i] != 0 and not visited[data[node + i]]:
                visited[data[node + i]] = True
                newqueue.append(data[node + i])
            elif data[node + i] == 0 and not visited[node + i]:
                visited[node + i] = True
                newqueue.append(node + i)
    findqueue = newqueue
    if 100 in findqueue:
        break
print(cnt)