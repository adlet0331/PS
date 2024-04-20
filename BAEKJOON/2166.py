N = int(input())
data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append((a, b))
# N = 10,000
# S = 1/2 | x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3 |
result = 0
(x1, y1) = data[0]
for i in range(1, N-1):
    (x2, y2) = data[i]
    (x3, y3) = data[i+1]
    result += 0.5 * (x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)
print(abs(round(result, 1)))