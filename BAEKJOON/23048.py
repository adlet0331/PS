N = int(input())

isdcml = [1 for _ in range(N + 1)]
dcml_cnt = 1
for i in range(2, N+1):
    if isdcml[i] == 1:
        dcml_cnt += 1
        for j in range(i, N + 1, i):
            isdcml[j] = dcml_cnt
isdcml = isdcml[1:]
print(dcml_cnt)
print(*isdcml, sep=" ")