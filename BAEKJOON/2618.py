'''
N = 1000
W = 1000

dp = 2 * 1000
O (N ^ 2) 까지 가능
과거를 다 돌아보자

아이디어 1
- dp[i][0], dp[i][1]: i번 사건을 1번 경찰차, 2번 경찰차가 해결 한경우 상태 저장

아이디어 2 (컨닝)
- dp[a][b]: 1번 경찰차가 마지막으로 a번, 2번 경찰차가 마지막으로 b를 해결한 최소 경로 (cnt) 저장
'''

N = int(input())
num = int(input())
data = [(1, 1)]
for _ in range(num):
    data.append(list(map(int, input().split(" "))))

def getdist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 아이디어 2
# 사각형 껍질을 채워가는 느낌
dp = [[0 for _ in range(num + 1)] for _ in range(num + 1)]
for index in range(1, num+1):
    for index2 in range(0, index):
        

# 아이디어 1, 틀림
# (movecnt, car1 pos, car2 pos)
# dp = [[(0, (1, 1), (N, N), [])]]
# for i in range(num):
#     target = data[i]
#     bcarlist = dp[-1]
#     validlist1 = []
#     validlist2 = []
#     mincnt1 = 100000000
#     mincnt2 = 100000000
#     for (cnt, c1pos, c2pos, log) in bcarlist:
#         # Move car 1
#         ccnt1 = getdist(target, c1pos)
#         if cnt + ccnt1 < mincnt1:
#             mincnt1 = cnt + ccnt1
#             validlist1.clear()
#             validlist1.append((cnt + ccnt1, target, c2pos, log + [1]))
#         elif cnt + ccnt1 == mincnt1:
#             validlist1.append((cnt + ccnt1, target, c2pos, log + [1]))
#         # Move car 2
#         ccnt2 = getdist(target, c2pos)
#         if cnt + ccnt2 < mincnt2:
#             mincnt2 = cnt + ccnt2
#             validlist2.clear()
#             validlist2.append((cnt + ccnt2, c1pos, target, log + [2]))
#         elif cnt + ccnt2 == mincnt2:
#             validlist2.append((cnt + ccnt2, c1pos, target, log + [2]))
        
#     dp.append(validlist1 + validlist2)

# mincnt = 1000000
# minlog = -1
# for (cnt, _, _, log) in dp[-1]:
#     if cnt < mincnt:
#         mincnt = cnt
#         minlog = log

# print(mincnt)
# for i in minlog:
#     print(i)
