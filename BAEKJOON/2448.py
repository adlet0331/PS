from math import log2
# 3×2_k
N = int(input())
k = int(log2(N//3))
onelinecnt = N * 2 - 1
sdata = [[True], [False, True], [True, True, True]]
def get_foldedlist(inplist):
    retlist = inplist[::-1]
    retlist += inplist[1:]
    return retlist
for _ in range(k):
    beforelen = len(sdata)
    for nlen in range(beforelen + 1, beforelen * 2 + 1):
        newdata = [False for _ in range(beforelen * 2 + 1 - nlen)]
        newdata += get_foldedlist(sdata[nlen - beforelen - 1])
        sdata.append(newdata)

for i in range(N):
    print(" " * (N - i - 1), end = "")
    for isfilled in get_foldedlist(sdata[i]):
        print("*" if isfilled else " ", end = "")
    print(" " * (N - i - 1), end = "")
    if i != N-1:
        print("")