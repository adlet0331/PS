import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결된 node가 2개 이상이면 단절점
# 단, cycle 판별해서 그 위에 있으면 cycle 하나당 상한 하나씩 증가
# 모든 cycle 종류 구하는 알고리즘 -> DFS O(E)
# 시간초과 / 메모리 초과 당함
cycles = set()
def searchcycle(node, route):
    for nextnode in graph[node]:
        if nextnode not in route:
            searchcycle(nextnode, route + [nextnode])
        elif nextnode != route[-2]:
            cycles.add(tuple(sorted(route[route.index(nextnode):])))
searchcycle(1, [1])
apmaxlimits = [2 for _ in range(V + 1)]
for cycle in cycles:
    for i in cycle:
        apmaxlimits[i] += 1
appoints = []
for i in range(1, V + 1):
    if apmaxlimits[i] <= len(graph[i]):
        appoints.append(i)
print(len(appoints))
print(*appoints, sep=" ")