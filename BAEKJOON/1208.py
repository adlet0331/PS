N, S = map(int, input().split())
data = list(map(int, input().split()))

# N: 1 ~ 40
# 2 ^ 40 불가능
# 20 / 20 으로 나눠서 구하기 -> 2 ^ 20 = 1,000,000
M = N // 2
def filldict(data):
    resdict = {}
    size = len(data)
    bitmask = 1
    while bitmask < 1 << size:
        key = 0
        for i in range(size):
            if bitmask & (1 << i):
                key += data[i]
        if key in resdict:
            resdict[key] += 1  
        else:
            resdict[key] = 1
        bitmask += 1
    return resdict

leftsums = filldict(data[:M])
rightsums = filldict(data[M:])
cnt = 0
for lkey, lvalue in leftsums.items():
    if S - lkey in rightsums:
        cnt += lvalue * rightsums[S - lkey]
if S in leftsums:
    cnt += leftsums[S]
if S in rightsums:
    cnt += rightsums[S]
print(cnt)