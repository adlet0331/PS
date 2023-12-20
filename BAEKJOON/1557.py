'''
미리 2^30개 개수 셀 수 있도록 해두자

이분 탐색으로 하는데, 그럼 30번 안에 찾을 수 있음

1 ~ N 까지 제곱ㄴㄴ수를 O(log N) 안에 찾을 수 있어야 함

포함배제 원리로 해보자 이전에 풀었던거랑 비슷하긴 한데 어떻게 저 시간 복잡도가 나오냐? 

itertools의 combination을 쓰면 안되나? 
다시 생각해보니 맞는것 같다.. queue를 써서 잘 잘 해보자!
'''
demicalsquares = []
notDemicalTrueList = [False for _ in range(50000 + 1)]

for i in range(2, 50000):
    if not notDemicalTrueList[i]:
        demicalsquares.append(i ** 2)
        for j in range(1, 50000 // i + 1):
            notDemicalTrueList[i * j] = True

dlen = len(demicalsquares)
K = int(input())

def countcnt(x):
    isXsq = False
    for dems in demicalsquares:
        if x % dems == 0:
            isXsq = True
            break
    cnt = x
    q = [(1, -1, -1)]
    while q:
        n, sindex, porm = q.pop()
        for i in range(sindex + 1, dlen):
            n1 = n * demicalsquares[i]
            if n1 > x:
                break
            cnt += porm * (x // n1)
            q.append((n1, i, -porm))
    return cnt, isXsq

findingNum, fscnt = 1 << 31, 30

while True:
    cnt, sq = countcnt(findingNum)
    if K > cnt:
        findingNum += 1 << fscnt
    elif K < cnt or (cnt == K and sq):
        findingNum -= 1 << fscnt
    else:
        break
    fscnt -= 1
    # print(f"sq: {sq} findingnum: {findingNum} fscnt: {fscnt}, cnt: {cnt}")
print(findingNum)