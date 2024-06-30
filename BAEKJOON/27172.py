import sys
input = sys.stdin.readline
N = int(input())
datas = list(map(int, input().split()))
# N = 10^5. data는 모두 다름. data <= 10^6
dwithidx = [(datas[i], i) for i in range(N)]
dwithidx.sort(key=lambda x: x[0])
# key: data num. item: result
adict = {}
for (num, index) in dwithidx:
    adict[num] = 0

# O(10^5 * (100001 // data))
for data in datas:
    for num in range(data * 2, 1000001, data):
        if num in adict:
            adict[data] += 1
            adict[num] -= 1

result = [0 for _ in range(N)]
for (num, index) in dwithidx:
    result[index] = adict[num]
print(*result, sep=" ")