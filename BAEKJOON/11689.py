N = int(input())
# 최대 공약수가 1인 개수 (1 ~ N)
demicals = []
maxDemical = int(N ** 0.5) + 2
notDemicalTrueList = [False for _ in range(maxDemical + 1)]
for i in range(2, maxDemical + 1):
    if not notDemicalTrueList[i]:
        demicals.append(i)
        for j in range(1, maxDemical // i + 1):
            notDemicalTrueList[i * j] = True
ndems = []
NN = N
for dec in demicals:
    while NN % dec == 0:
        if dec not in ndems:
            ndems.append(dec)
        NN = NN // dec
if NN > 1:
    ndems.append(NN)
cnt = N
for i in range(1, 1 << len(ndems)):
    bflag = bin(i)[2:][::-1]
    pmflag = 1
    acnt = N
    index = 0
    for bb in bflag:
        if bb == "1":
            pmflag *= -1
            acnt = acnt // ndems[index]
        index += 1
    cnt += pmflag * acnt
print(int(cnt))
        