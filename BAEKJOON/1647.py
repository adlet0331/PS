from queue import PriorityQueue
import sys
input = sys.stdin.readline
# N=10^5, M=10^6
N, M = map(int, input().split())
# 마을을 2개의 사이클로 분리, 유지비 최소로
edata = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edata[a].append((b, c))
    edata[b].append((a, c))
# 최소 스팬트리 - 엣지 최대값이 최소값인가? yes
pq = PriorityQueue()
result = 0
maxeval = 0
cnt = N - 1
curnode = 1
checked = [False if i != 1 else True for i in range(N+1)]
while cnt > 0:
    for (nextnode, val) in edata[curnode]:
        if not checked[nextnode]:
            pq.put((val, nextnode))
    while pq:
        (val, nextnode) = pq.get()
        if not checked[nextnode]:
            #print(nextnode)
            maxeval = max(maxeval, val)
            checked[nextnode] = True
            curnode = nextnode
            result += val
            cnt -= 1
            break

print(result - maxeval)