import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
dp = [-1000000001]
trace = [-1 for _ in range(N + 1)]

for i in range(1, N + 1):
    mindex = bisect.bisect_left(dp, arr[i]) - 1
    trace[i] = mindex + 1
    if mindex == len(dp) - 1:
        dp.append(arr[i])
    elif dp[mindex + 1] > arr[i]:
        dp[mindex + 1] = arr[i]

print(len(dp) - 1)
cnt = len(dp) - 1
#answer = ''  이렇게 하니까 시간 초과 남 ㅎㅎ;; 억울하다!
#for i in range(N, 0, -1):
#    if trace[i] == cnt:
#        answer = f'{arr[i]} {answer}'
#        cnt -= 1
#    if cnt == 0:
#        break
#print(answer)
answer = []
for i in range(N, 0, -1):
    if trace[i] == cnt:
        answer.append(arr[i])
        cnt -= 1
        if cnt == 0:
            break
print(*answer[::-1])