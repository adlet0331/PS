import sys
from math import sin, cos, pi, sqrt

for line in sys.stdin:
    r, h, d1, A1, d2, A2 = map(float, line.split(" "))
    radian_constant = pi / 180 * (r / sqrt(abs(h ** 2 + r ** 2)))

    A2 = abs(A2 - A1)
    if A2 > 180:
        A2 = 360 - A2
    x1, y1 = d1, 0
    x2, y2 = d2 * cos(radian_constant * A2), d2 * sin(radian_constant * A2)
    print(f"{round(sqrt(abs((x1 - x2) ** 2 + (y1 - y2) ** 2)), 2):.2f}")