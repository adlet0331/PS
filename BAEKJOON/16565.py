# 수학, N개 뽑았을 때 포카드가 나올 경우의 수 % 10007
N = int(input())
result = 0
def comb(a, b):
    cnt = 1
    for i in range(b):
        cnt *= (a - i)
        cnt = cnt // (i + 1)
    return cnt
if N < 4:
    print(0)
else:
    for i in range(1, N // 4 + 1):
        num = 1
        num *= comb(13, i) * comb(52 - 4*i, N - 4*i)
        result += (1 if i % 2 == 1 else -1) * num % 10007

    print(result % 10007)