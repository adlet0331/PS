N, M, R = map(int, input().split())
itemdata = [0] + list(map(int, input().split()))
graph = [[10000000 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(R):
    s, e, l = map(int, input().split())
    graph[s][e] = l
    graph[e][s] = l
for k in range(1, N+1):
    graph[k][k] = 0
    for start in range(1, N+1):
        for end in range(1, N+1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])
result = 0
for start in range(1, N+1):
    cnt = 0
    for i in range(1, N+1):
        if graph[start][i] <= M:
            cnt += itemdata[i]
    result = max(result, cnt)
print(result)