import sys
input = sys.stdin.readline
M = int(input())
T = 1000000007
# M = 10^4
def get_ie(num, pnum, mnum):
    result = 1
    while pnum > 0:
        if pnum % 2 != 0:
            result = (result * num) % mnum
        pnum //= 2
        num = (num * num) % mnum
    return result
result = 0
for _ in range(M):
    a, b = map(int, input().split())
    result += b * get_ie(a, T - 2, T)
print(result % T)