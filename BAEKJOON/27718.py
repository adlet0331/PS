import sys

N = int(input())
lines = []
# y = ax + b 
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    lines.append((x1, y1, x2, y2))
result = [[3 for _ in range(N)] for _ in range(N)]

def cross_product(x0, y0, x1, y1, x2, y2):
    return x0 * y1 + x1 * y2 + x2 * y0 - x0 * y2 - x1 * y0 - x2 * y1

# cross 다 했을 때, 부호가 같은것이 있을 때 - 교차 X (0)
# cross 다 했을 때, 0이 1개 있을 때 - 끝점 (1)
# cross 다 했을 때, 부호가 둘 다 다를 때 - 교차 (2)
# cross 다 했을 때, 모두 0이 나올 때 - 무수히 많거나 없음 (0 or 3)

for i in range(N):
    for j in range(i + 1, N):
        xi1, yi1, xi2, yi2 = lines[i]
        xj1, yj1, xj2, yj2 = lines[j]

        ci1 = cross_product(xi1, yi1, xi2, yi2, xj1, yj1)
        ci2 = cross_product(xi1, yi1, xi2, yi2, xj2, yj2)
        cj1 = cross_product(xj1, yj1, xj2, yj2, xi1, yi1)
        cj2 = cross_product(xj1, yj1, xj2, yj2, xi2, yi2)

        if ci1 * ci2 > 0 or cj1 * cj2 > 0:
            result[i][j] = 0
            result[j][i] = 0
            continue
        elif ci1 * ci2 < 0 and cj1 * cj2 < 0:
            result[i][j] = 2
            result[j][i] = 2
            continue
        elif ci1 * ci2 == 0 or cj1 * cj2 == 0:
            if ci1 == 0 and ci2 == 0 and cj1 == 0 and cj2 == 0:
                # y축 평행
                if xi1 == xi2:
                    (xi1, xi2, yi1, yi2) = (xi1, xi2, yi1, yi2) if yi1 < yi2 else (xi2, xi1, yi2, yi1)
                    (xj1, xj2, yj1, yj2) = (xj1, xj2, yj1, yj2) if yj1 < yj2 else (xj2, xj1, yj2, yj1)
                    if yj2 < yi1 or yi2 < yj1:
                        result[i][j] = 0
                        result[j][i] = 0
                        continue
                    elif yj2 == yi1 or yi2 == yj1:
                        result[i][j] = 1
                        result[j][i] = 1
                        continue
                    else:
                        continue
                else:
                    (xi1, xi2, yi1, yi2) = (xi1, xi2, yi1, yi2) if xi1 < xi2 else (xi2, xi1, yi2, yi1)
                    (xj1, xj2, yj1, yj2) = (xj1, xj2, yj1, yj2) if xj1 < xj2 else (xj2, xj1, yj2, yj1)
                    if xj2 < xi1 or xi2 < xj1:
                        result[i][j] = 0
                        result[j][i] = 0
                        continue
                    elif xj2 == xi1 or xi2 == xj1:
                        result[i][j] = 1
                        result[j][i] = 1
                        continue
                    else:
                        continue
            else:
                result[i][j] = 1
                result[j][i] = 1
                continue
for res in result:
    print(*res, sep='')