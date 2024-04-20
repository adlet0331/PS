import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False for _ in range(N+1)]
    cnt = N
    for i in range(1, N+1):
        if visited[i]:
            continue
        inroute = [i]
        visited[i] = True
        while not visited[graph[i]]:
            visited[graph[i]] = True
            inroute.append(graph[i])
            i = graph[i]
        iscycle = False
        for j in inroute:
            iscycle = iscycle or j == graph[i]
            if iscycle:
                cnt -= 1
    sys.stdout.write(f"{cnt}\n")