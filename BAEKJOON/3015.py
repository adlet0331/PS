import sys
input = sys.stdin.readline
N = int(input())
data = []
# N = 500000 = 5 * 10^5. data<2^3. O(NlogN) 내로 해결해야
# 항상 data 안은 내림차순으로 존재. 새로 들어온 데이터가 들어가면 내림차순 만족할 때 까지 data pop 하기
result = 0
for _ in range(N):
    num = int(input())
    # print(result, data)
    while data and data[-1][0] < num:
        result += data.pop()[1]
    if data and data[-1][0] == num:
        result += data[-1][1]
        result += 0 if len(data) == 1 else 1
        data[-1][1] += 1
    else:
        result += 1 if data else 0
        data.append([num, 1])    
print(result)