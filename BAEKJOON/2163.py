N, M = map(int, input().split(" "))

print(N * M - 1) #?? 정답나옴

# def get_min_split(row, column):
#     if row < column:
#         row, column = column, row
#     dp = [[0] * (column + 1) for _ in range(row + 1)]

#     def get_val(a, b):
#         return dp[a][b] if a > b else dp[b][a]

#     # Always, r >= c
#     for r in range(2, row + 1):
#         for c in range(1, r + 1 if r + 1 < column + 1 else column + 1):
#             cnt = 100000
#             # in a row
#             for i in range(1, int(r / 2) + 1):
#                 val = get_val(r-i, c) + get_val(i, c) + 1
#                 if cnt > val:
#                     cnt = val
#             # in a column
#             for i in range(1, int(c / 2) + 1):
#                 val = get_val(c-i, r) + get_val(i, r) + 1
#                 if cnt > val:
#                     cnt = val
#             dp[r][c] = cnt
#     #print(dp)
#     return get_val(row, column)

# print(get_min_split(N, M))