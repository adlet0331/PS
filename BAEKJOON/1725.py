'''
N <= 10^5
O(NlogN) 안에 해결해야함
Stack으로 O(n) 으로 해결할 수 있음. 강해져서 왔다!
'''
import sys
from collections import deque
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
stack = deque()
#(index, height)
stack.append((-1, 0))
result = 0
for i in range(N+1):
    # Stack의 Top 보다 클 때, 삽입 후 넘어감
    curr = arr[i] if i != N else -1
    if stack[-1][1] <= curr:
        stack.append((i, curr))
        continue
    # curr이 현재 stack의 Top 보다 작을 때
    while len(stack) > 1:
        (pindex, plen) = stack.pop()
        result = max(result, plen * (i - stack[-1][0] - 1))
        if stack[-1][1] <= curr:
            stack.append((i, curr))
            break
print(result)