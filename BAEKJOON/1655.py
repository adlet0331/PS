from heapq import heappush, heappop

N = int(input())
idata = []
for _ in range(N):
    idata.append(int(input()))

lheap = [] # Max heap
rheap = [] # Min heap

lheap.append(max(-idata[0], -idata[1]))
rheap.append(max(idata[0], idata[1]))

print(idata[0])
print(-lheap[0])

for index in range(2, N):
    if index % 2 == 0: # [1, 2] - [3, 5]  <= 4 
        if rheap[0] < idata[index]:
            rhead = heappop(rheap)
            heappush(lheap, -rhead)
            heappush(rheap, idata[index])
        else: # [1, 3] - [4, 5] <= 2
            heappush(lheap, -idata[index])
    else: # [1, 2, 4] - [5, 6]  <= 3
        if lheap[0] + idata[index] < 0:
            lhead = -heappop(lheap)
            heappush(rheap, lhead)
            heappush(lheap, -idata[index])
        else: # [1, 2, 4] - [5, 6]  <= 7
            heappush(rheap, idata[index])

    print(-lheap[0])