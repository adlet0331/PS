N = int(input())
data = list(map(int, input().split()))

dp = [data[0]]
for element in data[1:]:
    if element > dp[-1]:
        dp.append(element)
    else:
        front = 0
        back = len(dp) - 1
        while back > front:
            mid = (back + front) // 2
            if dp[mid] < element:
                front = mid + 1
            else:
                back = mid
        dp[back] = element

print(len(dp))

## O(n^2), 시간 초과됨 
# dp = [0 for _ in range(N)]
# def recurse(start):
#     if dp[start] != 0:
#         return dp[start]
#     cnt = 1
#     lnum = 1000001
#     for i in range(start + 1, N):
#         if data[start] < data[i] and lnum > i:
#             cnt = max(cnt, recurse(i) + 1)
#             lnum = i
#     dp[start] = cnt
#     return cnt


# mcnt = 0
# for i in range(N):
#     if dp[i] != 0:
#         continue
#     mcnt = max(mcnt, recurse(i))
# print(mcnt)