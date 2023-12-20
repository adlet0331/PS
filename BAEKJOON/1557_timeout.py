# K번째 제곱 ㄴㄴ수를 구해야함

"""
K가 최대 10^9

포함배제원리
O(logN)으로 해결해야 함
i < log(2 * K) 인 i에 대해 i^2의 배수들이 제곱 ㄴㄴ 수가 아니므로 K에 더해가자
--> K에 더해가면 K가 커지면서 처음에 포함된 배수들이 포함이 안되어 버리는데, 어떡하지! 어떡하지..
--> 리스트 써서 remove를 해야하나 그러자!
대충 찾아보니 10^8번 연산에 1초 걸린다는디
아 그러면 remove 못쓰는데, remove 쓰면 O(N)짜리를 여러번 해야함;;
--> 자 그럼 수학으로 푸는 수 밖에..
--> 약간 이진 탐색 느낌으로 가자! K 만큼 탐색하면 제곱 ㄴㄴ수가 A개인지 나오겠지. 그럼 K+1 부터 K+A 만큼 또 탐색을 해. 이걸 계속 반복하면 되지 않을까? 좋아!!

log N * (log N) ^ 2번 연산함 가능할듯?
2^2 -> K + K / 4 
3^3 -> K + K / 9 - K / 36
5^5 -> K + K / 25 - K / 225 - K / 100
7^7 -> K + K / 49 - {K / (7*5)^2 + K / (7*3)^2 + K / (7*2)^2} + {K / (7*5*3)^2 + K / (7*5*2)^2 + K / (7*5*3)^2 + K / (7*5*3)^2}
"""
from itertools import combinations

K = int(input())
cdemical = 2
demicals = []

demicals = []
notDemicalTrueList = [False for _ in range(31701)]

for i in range(2, 31700):
    if not notDemicalTrueList[i]:
        demicals.append(i ** 2)
        for j in range(1, 31700 // i + 1):
            notDemicalTrueList[i * j] = True

# toresult 까지 제곱 ㄴㄴ수의 개수
cnt = 0
# 현재 탐색할 시작 지점
start = 1
# 현재 탐색할 범위의 수
end = 0
while cnt < K:
    # 이전 탐색범위 제외
    start = end + 1
    # 현재 탐색 범위 남은 cnt 만큼 더해주기
    end += (K - cnt)
    # 미리 더해주기
    cnt += (K - cnt)
    # 가장 처음 소수
    # 현재 최대값 보다 현재 판별하고 있는 소수의 제곱이 작야아 탐색, 아님 의미가 없음 
    print(f"start: {start}, end: {end}")
    # while cdemical ** 2 < end:
    #     demicals.append(cdemical ** 2)
    #     # cdemical 다음 소수로
    #     while True:
    #         cdemical += 1
    #         flag = False
    #         for dem in demicals:
    #             if (cdemical ** 2) % dem == 0:
    #                 flag = True
    #                 break
    #         if not flag:
    #             break
    # print(f"curr demicals: {demicals}")
    # K=12345 일때도 겁나 오래 걸림.. 어떡해! combinations 최적화를 해야하나..?
    for i in range(1, len(demicals)+1):
        for elems in combinations(demicals, i):
            dpow = 1
            for elem in elems:
                dpow *= elem
                if dpow > end:
                    break
            if dpow > end:
                continue
            cnt += ((-1) ** (i)) * ((end) // dpow - (start - 1) // dpow)
    print(f"cnt: {cnt}")
print(end)