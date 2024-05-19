import sys
input = sys.stdin.readline
while True:
    # N: 100, M: 5000
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    graph = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node):
        for i in range(N):
            if len(graph[i]) < 2:
                return True
        visited[node] = True
        childnum = 0
        for child in graph[node]:
            if visited[child]:
                continue
            childnum += 1
            dfs(child)
        return childnum != 1
    
    # 단절선 존재 유무 찾기
    # 모든 node에서 dfs 돌려서 child 2개 이상 돌면 단절선임 
    for i in range(N):
        visited = [False for _ in range(N)]
        # 단절선 발견 시
        if dfs(i):
            print("Yes")
            break
        if i == N-1:
            print("No")