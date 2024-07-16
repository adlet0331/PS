# 집합 문제
N, M = map(int, input().split())
precursors = list(map(int, input().split()))
pcount, precursors = precursors[0], precursors[1:]
setdatas = []
for _ in range(M):
    setdatas.append(list(map(int, input().split()))[1:])
pchecked = [False for i in range(M)]
if pcount > 0:
    fqueue = precursors.copy()
    while fqueue:
        cnode = fqueue.pop(0)
        for i in range(M):
            if cnode in setdatas[i]:
                pchecked[i] = True
                for snode in setdatas[i]:
                    if not snode in precursors:
                        precursors.append(snode)
                        fqueue.append(snode)
# precursors 완성. 이제 나머지들은 다 거짓말 해도 됨
# print(pchecked)
print(M - pchecked.count(True))