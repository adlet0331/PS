N = int(input())
dlist = []
for _ in range(N):
    dlist.append(input().split())
dlist.sort(reverse=True)
anthouse = {}
for data in dlist:
    datalen = int(data[0])
    chouse = anthouse
    for i in range(1, datalen + 1):
        if data[i] not in chouse:
            chouse[data[i]] = {}
        chouse = chouse[data[i]]
fqueue = []
initkeys = list(anthouse.keys())
initkeys.sort(reverse=True)
for key in initkeys:
    fqueue.append((key, 1, anthouse[key]))
while fqueue:
    node, fnum, childs = fqueue.pop()
    print("-" * 2 * (fnum-1) + node)
    childkeys = list(childs.keys())
    childkeys.sort(reverse=True)
    for key in childkeys:
        fqueue.append((key, fnum + 1, childs[key]))