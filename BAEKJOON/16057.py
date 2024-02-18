from math import sqrt, gcd
import sys
input = sys.stdin.readline

N = int(input())
# 모든 꼭짓점은 정수
# 꼭짓점들이 N개 있고 각 꼭짓점들은 선분으로 이어짐
# 내 땅 안의 점의 개수 세기
# 점들은 선분을 이루는 순서대로 주어짐

cordinates = []
for _ in range(N):
    x, y = map(int, input().split())
    cordinates.append((x,y))
cordinates.append(cordinates[0])

# 픽의 정리
# A: 다각형의 넓이, b: 변 위에 있는 점의 수, i: 내부의 점
# i = A - b / 2 + 1

# A는 헤론의 공식 + 오목 고려해서 구하기
# b는 걍 잘 구하면 됨
A = 0
(x, y) = cordinates[0]
# O(N)
for i in range(1, N-1):
    (x1, y1) = cordinates[i]
    (x2, y2) = cordinates[i+1]
    # 외적으로 시계 반시계 판별
    sign = -1
    if (x1 - x) * (y2 - y) - (x2 - x) * (y1 - y) < 0:
        sign = 1
    a = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    b = sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
    c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    s = (a + b + c) / 2
    A += (sign * sqrt(abs(s * (s - a)* (s - b)* (s - c))))
A = abs(A)

b = 0
for i in range(N):
    (x1, y1) = cordinates[i]
    (x2, y2) = cordinates[i+1]
    if x2 == x1:
        b += abs(y1 - y2)
    elif y2 == y1:
        b += abs(x1 - x2)
    else:
        b += gcd(abs(y2 - y1), abs(x2 - x1))
# i = A - b / 2 + 1
print(round(A - b / 2 + 1))

# x축에 평행한 직선 그어서 교차점 찾고 그걸로 수 세기 시간초과
# minx = 10**6
# maxx = - 10**6
# miny = 10**6
# maxy = - 10**6
# for (x, y) in cordinates:
#     if x < minx:
#         minx = x
#     if x > maxx:
#         maxx = x
#     if y < miny:
#         miny = y
#     if y > maxy:
#         maxy = y
# total_cnt = 0
# for cy in range(miny, maxy + 1):
#     cyxlist = []
#     skipflag = False
#     for i in range(N):
#         (x1, y1) = cordinates[i]
#         (x2, y2) = cordinates[i+1]
#         if y1 == cy and y2 == cy:
#             skipflag = True
#             break
#         # 교차 하는 경우 찾기
#         if (y1 <= cy and cy < y2) or (y2 < cy and cy <= y1):
#             if cy == y1:
#                 cyxlist.append(x1)
#             elif x1 != x2:
#                 cyxlist.append(x1 + x2 / (y2 - y1))
#             elif x1 == x2:
#                 cyxlist.append(x1)
#     if skipflag:
#         continue
    
#     cyxlist.sort()
#     for i in range(len(cyxlist) // 2):
#         cyx1 = floor(cyxlist[i * 2 + 1]) if floor(cyxlist[i * 2 + 1]) != cyxlist[i * 2 + 1] else cyxlist[i * 2 + 1] - 1
#         cyx2 = ceil(cyxlist[i * 2]) if ceil(cyxlist[i * 2]) != cyxlist[i * 2] else cyxlist[i * 2] + 1
#         total_cnt += (cyx1 - cyx2 + 1)
#     #print(f"cy : {cy}, cyxlist : {cyxlist}")
# print(total_cnt)


# 전체 탐색 시간초과
# W*H*O(n)
# x축과 평행한 선분을 그어 몇 번 교차 하는지로 내부/외부 판별
# total_cnt = 0     
# for cx in range(minx, maxx + 1):
#     for cy in range(miny, maxy + 1):
#         cross_cnt = 0
#         for i in range(N):
#             (x1, y1) = cordinates[i]
#             (x2, y2) = cordinates[i+1]
#             # 교차하고, 오른쪽에 있을 경우만
#             if (y1 < cy and cy < y2) or (y2 < cy and cy < y1):
#                 if cx < x1 + x2 / (y2 - y1):
#                     cross_cnt += 1
#         if cross_cnt % 2 == 1:
#             total_cnt += 1
# print(total_cnt)