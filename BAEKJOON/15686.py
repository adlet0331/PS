N, M = map(int, input().split())
houses = []
chickens = []
# houses = 100, chickens = 13
# 최단거리 구하는 시간: 100 * 13 = 1300
# 13 C 6 = 1716
# 조합으로 해도 되겠다
MM = 0
for i in range(N):
    clist = list(map(int, input().split()))
    for j in range(N):
        if clist[j] == 1:
            houses.append((i, j))
        elif clist[j] == 2:
            chickens.append((i, j))
            MM += 1
binaryflag = (1 << M) - 2
maxbinaryflag = (1 << MM) - 2
result = 10 ** 5
while binaryflag <= maxbinaryflag:
    binaryflag += 1
    if str(bin(binaryflag)).count("1") != M:
        continue
    bflagstr = str(bin(binaryflag))[::-1]
    fchickens = []
    for i in range(len(bflagstr)):
        if bflagstr[i] == "1":
            fchickens.append(chickens[i])
    # print(houses, fchickens)
    cnt = 0
    for house in houses:
        minlen = 10000
        for chicken in fchickens:
            minlen = min(minlen, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        cnt += minlen
        # print(minlen)
    result = min(result, cnt)
print(result)