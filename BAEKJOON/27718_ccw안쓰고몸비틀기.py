from decimal import Decimal
import sys

N = int(input())
lines = []
# y = ax + b 
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    a = ((y2 - y1) , (x2 - x1)) if x2 != x1 else "infinite"
    b = "infinite" if a == "infinite" else Decimal(y1 - ((y2 - y1) / (x2 - x1)) * x1)
    lines.append((a, b, (x1, y1), (x2, y2)) if y1 < y2 else (a, b, (x2, y2), (x1, y1)))
# print(*lines, sep="\n")
# 0 : 교점 x
# 1 : 교점 하나 있고, 한 선분의 끝점임
# 2 : 교점이 하나 있고, 두 선분의 끝점이 아님
# 3 : 교점 무수히 많음

result = [[3 for _ in range(N)] for _ in range(N)]
def isbetween(x1, x2, x):
    if (x1 < x and x < x2) or (x2 < x and x < x1):
        return True
    else:
        return False
def iseqorbetween(x1, x2, x):
    if (x1 <= x and x <= x2) or (x2 <= x and x <= x1):
        return True
    else:
        return False
#완전탐색? O(N^2) 4,000,000 할만하네
for i in range(N):
    for j in range(i + 1, N):
        (a1, b1, (x11, y11), (x12, y12)) = lines[i]
        (a2, b2, (x21, y21), (x22, y22)) = lines[j]
        if i == j:
            result[i][j] = 3
            result[j][i] = 3
            continue
        # 둘 다 y축에 평행 
        elif a1 == "infinite" and a2 == "infinite":
            if x11 != x21:
                result[i][j] = 0
                result[j][i] = 0
                continue
            elif x11 == x21:
                if y11 == y22 or y12 == y21:
                    result[i][j] = 1
                    result[j][i] = 1
                    continue
                elif iseqorbetween(y11, y12, y21) or iseqorbetween(y11, y12, y22) or iseqorbetween(y21, y22, y11) or iseqorbetween(y21, y22, y12):
                    result[i][j] = 3
                    result[j][i] = 3
                    continue
                else:
                    result[i][j] = 0
                    result[j][i] = 0
                    continue
        # 기울기가 무한대가 아니지만 기울기가 같음
        elif a1 != "infinite" and a2 != "infinite" and a1[0] * a2[1] == a2[0] * a1[1]:
            if b1 != b2:
                result[i][j] = 0
                result[j][i] = 0
                continue
            elif b1 == b2:
                if y12 == y21 or y11 == y22:
                    result[i][j] = 1
                    result[j][i] = 1
                    continue
                elif y12 < y21 or y22 < y11:
                    result[i][j] = 0
                    result[j][i] = 0
                    continue
                elif iseqorbetween(y11, y12, y21) or iseqorbetween(y11, y12, y22) or iseqorbetween(y21, y22, y11) or iseqorbetween(y21, y22, y12):
                    result[i][j] = 3
                    result[j][i] = 3
                    continue
                else:
                    raise IndexError("ERROR 2")
        # 두 선분의 기울기가 같지 않음
        elif a1 == "infinite" or a2 == "infinite" or a1[0] * a2[1] != a2[0] * a1[1]:
            if (x11, y11) == (x21, y21) or (x12, y12) == (x21, y21) or (x11, y11) == (x22, y22) or (x12, y12) == (x22, y22):
                result[i][j] = 1
                result[j][i] = 1
                continue
            # xx, yy 두 직선 교점. infinite가 있으면 a1이 무한대
            if a2 == "infinite":
                (a1, b1, (x11, y11), (x12, y12)), (a2, b2, (x21, y21), (x22, y22)) = (a2, b2, (x21, y21), (x22, y22)), (a1, b1, (x11, y11), (x12, y12))
            xx = Decimal((float)(b1 - b2) / ((a2[0] * a1[1] - a1[0] * a2[1]) / (a2[1] * a1[1]))) if a1 != "infinite" else x11
            yy = Decimal((a2[0] / a2[1]) * float(xx) + float(b2))
            # print(xx, yy)
            # 교점이 한 선분의 끝점임
            if (xx == x11 and yy == y11 and iseqorbetween(x21, x22, xx) and iseqorbetween(y21, y22, yy)) or (xx == x12 and yy == y12 and iseqorbetween(x21, x22, xx) and iseqorbetween(y21, y22, yy)) or (xx == x21 and yy == y21 and iseqorbetween(x11, x12, xx) and iseqorbetween(y11, y12, yy)) or (xx == x22 and yy == y22 and iseqorbetween(x11, x12, xx) and iseqorbetween(y11, y12, yy)):
                result[i][j] = 1
                result[j][i] = 1
                continue
            # 선끼리 교점이 있음
            elif ((a1 == "infinite" and isbetween(y11, y12, yy)) or (a1 != "infinite" and (a1[0] == 0 and isbetween(x11, x12, xx))) or (a1 != "infinite" and a1[0] != 0 and isbetween(x11, x12, xx) and isbetween(y11, y12, yy))) and (a2[0] == 0 or isbetween(y21, y22, yy)) and isbetween(x21, x22, xx):
                result[i][j] = 2
                result[j][i] = 2
                continue
            # 교점이 한 선분의 바깥에 있음
            else:
                result[i][j] = 0
                result[j][i] = 0
        else:
            raise IndexError("ERROR 1")
for res in result:
    print(*res, sep='')