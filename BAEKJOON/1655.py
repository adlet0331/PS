import heapq

N = int(input())
print("N:", N)
idata = []
for _ in range(N):
    idata.append(int(input()))

heap = []

for cnt in range(N):
    heapq.heappush(heap, idata[cnt])
    