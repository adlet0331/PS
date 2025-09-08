import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
collines = [set() for _ in range(H)]
for _ in range(M):
    h, b = map(int, input().split())
    collines[h-1].add(b)

def check_avaliable(addeds=[]):
    if len(addeds) >= 2:
        for i in range(len(addeds)):
            r1, c1 = addeds[i]
            for j in range(i+1, len(addeds)):
                r2, c2 = addeds[j]
                if r1 == r2 and abs(c1 - c2) == 1:
                    return False
    result = [i for i in range(N+1)]
    add_map = {}
    for r, c in addeds:
        add_map.setdefault(r, []).append(c)
    for h in range(H):
        if h in add_map:
            cols = sorted(collines[h])
            cols = sorted(cols + add_map[h])
        else:
            if not collines[h]:
                continue
            cols = sorted(collines[h])
        for left in cols:
            result[left], result[left + 1] = result[left + 1], result[left]
    for i in range(1, N+1):
        if result[i] != i:
            return False
    return True

avaliables = []
for row in range(H):
    for col in range(1, N):
        if (col in collines[row]) or (col-1 in collines[row]) or (col+1 in collines[row]):
            continue
        avaliables.append((row, col))

if check_avaliable():
    print(0)
    sys.exit(0)

for i in range(len(avaliables)):
    el1 = avaliables[i]
    if check_avaliable([el1]):
        print(1)
        sys.exit(0)

for i in range(len(avaliables)):
    r1, c1 = avaliables[i]
    for j in range(i+1, len(avaliables)):
        r2, c2 = avaliables[j]
        if r1 == r2 and abs(c1 - c2) == 1:
            continue
        if check_avaliable([avaliables[i], avaliables[j]]):
            print(2)
            sys.exit(0)

for i in range(len(avaliables)):
    r1, c1 = avaliables[i]
    for j in range(i+1, len(avaliables)):
        r2, c2 = avaliables[j]
        if r1 == r2 and abs(c1 - c2) == 1:
            continue
        for k in range(j+1, len(avaliables)):
            r3, c3 = avaliables[k]
            if (r1 == r3 and abs(c1 - c3) == 1) or (r2 == r3 and abs(c2 - c3) == 1):
                continue
            if check_avaliable([avaliables[i], avaliables[j], avaliables[k]]):
                print(3)
                sys.exit(0)

print(-1)
