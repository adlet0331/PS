from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, L = map(int, input().split())
arr = list(map(int, input().split()))

deq = deque()
for i in range(N):
    if deq and deq[0][0] <= i - L:
        deq.popleft()
    element = arr[i]
    while len(deq) >= 1 and element < deq[-1][1]:
        deq.pop()
    deq.append((i, element))
    print(str(deq[0][1]) + ' ')
print('\n')