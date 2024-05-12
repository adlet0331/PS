N = int(input())
erat_che = [True for _ in range(N + 1)]
erat_che[0], erat_che[1] = False, False
# 최대 3*10^5
decimals = []
for i in range(2, N + 1):
    if erat_che[i]:
        for j in range(2, N // i + 1):
            erat_che[i * j] = False
        decimals.append(i)
dp = [0 for _ in range(N + 1)]
start, end, maxindex = 0, 0, len(decimals)
result = 0
while end < maxindex:
    cnt = sum(decimals[start : end + 1])
    if cnt < N:
        end += 1
    elif cnt == N:
        result += 1
        start += 1
        end += 1
    elif cnt > N:
        start += 1
print(result)