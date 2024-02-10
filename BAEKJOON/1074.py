N, r, c = map(int, input().split(" "))

global CNT
global SFLAG
CNT = 0
SFLAG = False

def zz(minr, minc, maxr, maxc, range):
    global CNT
    global SFLAG
    if SFLAG:
        return
    isin = False
    if minr <= r and r <= maxr and minc <= c and c <= maxc:
        isin = True
    if not isin:
        CNT += range ** 2
        return
    if range == 1:
        if minr == r and minc == c:
            print(CNT)
            SFLAG = True
        else:
            CNT += 1
        return
    midr = (minr + maxr) // 2
    midc = (minc + maxc) // 2
    midrange = range // 2
    zz(minr, minc, midr, midc, midrange)
    zz(minr, midc + 1, midr, maxc, midrange)
    zz(midr + 1, minc, maxr, midc, midrange)
    zz(midr + 1, midc + 1, maxr, maxc, midrange)

zz(0, 0, 2 ** N-1, 2 ** N-1, 2 ** N)