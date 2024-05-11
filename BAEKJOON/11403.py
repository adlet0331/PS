N = int(input())
gdata = []
for _ in range(N):
    gdata.append(list(map(int, input().split())))
reachable = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    for snode in range(N):
        for enode in range(N):
            if gdata[snode][enode] == 1:
                reachable[snode][enode] = 1
                for onode in range(N):
                    if reachable[onode][snode] == 1:
                        reachable[onode][enode] = 1
for data in reachable:
    print(*data, sep=" ")