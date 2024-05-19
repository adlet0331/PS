import sys
input = sys.stdin.readline

N = int(input())
cnum = [0 for _ in range(N+1)]
nodes = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    nodes.append((a, b))
    cnum[a] += 1
    cnum[b] += 1
# 이어져있는 자식이 2개 이상이면 단절점. 트리는 모든선이 단절선이다
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print("yes" if cnum[b] > 1 else "no")
    if a == 2:
        print("yes")