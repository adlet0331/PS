import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
dp = [-1000000001]
trace = [-1 for _ in range(N + 1)]

# bisect_left 로 대체 가능
# arr[index] 보다 작은, 가장 큰 수가 있는 index
# def findSmallerMax(index):
#     num = arr[index]
#     start = 0
#     end = len(dp) - 1
#     while start + 1 < end:
#         mid = (start + end) // 2
#         if dp[mid] < num:
#             start = mid
#         elif dp[mid] > num:
#             end = mid
#         else:
#             return mid - 1
#     return start if dp[end] >= num else end

for i in range(1, N + 1):
    mindex = bisect.bisect_left(dp, arr[i]) - 1
    trace[i] = mindex + 1
    if mindex == len(dp) - 1:
        dp.append(arr[i])
    if dp[mindex + 1] > arr[i]:
        dp[mindex + 1] = arr[i]

print(len(dp) - 1)
cnt = len(dp) - 1
answer = ''
for i in range(N, 0, -1):
    if trace[i] == cnt:
        answer = f'{arr[i]} {answer}'
        cnt -= 1
    if cnt == 0:
        break
print(answer)