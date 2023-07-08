N = int(input())
data = list(map(int, input().split()))

def find_less_largest_index(dplist, num):
    front = 0
    back = len(dplist) - 1
    index = front + (back - front) // 2
    while front != back:
        index = front + (back - front) // 2
        if dplist[index] == num:
            return -1
        if dplist[index] < num:
            front = index
        else:
            back = index
    return index

dp = []
for element in data:
    if len(dp) == 0 or element > dp[-1]:
        dp.append(element)
    else:
        index = find_less_largest_index(dp, element)
        if index == -1:
            continue
        dp[index] = element

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