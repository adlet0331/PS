import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
sizes = list(map(int, input().split()))

ssizes = sizes.copy()
for i in range(M):
    for j in range(i+1, M):
        if sizes[i] + sizes[j] <= N:
            ssizes.append(sizes[i] + sizes[j])
ssizes = list(set(ssizes))
ssizes.sort()

# cnt[N] = cnt[A] + cnt[N - A]
cnt = [-1 for _ in range(N + 1)]
cnt[0] = 0
for ssize in ssizes:
    cnt[ssize] = 1

def get_cnt(num):
    if cnt[num] != -1:
        return cnt[num]
    else:
        mincnt = 100000
        for ssize in ssizes:
            if ssize > num:
                break
            for i in range(num // ssize, 0, -1):
                mincnt = min(mincnt, i + get_cnt(num - ssize * i))
        cnt[num] = mincnt
        return mincnt

result = get_cnt(N)
print(result if result != 100000 else -1)