N = int(input())
data = list(map(int, input().split()))
data.sort()

DEC = 1000000007
# 여기가 생각보다 오래 걸림. logN으로 해야 풀린다.
twopows = [1]
for i in range(1, N):
    twopows.append(twopows[i-1] * 2 % DEC)
result = 0
N = len(data)
for i in range(N):
    result += (twopows[i] - twopows[N - i - 1]) * (data[i] % DEC)
    if result > DEC:
        result %= DEC
print(result % DEC)