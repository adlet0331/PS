N = int(input())
keyword = input().split()
roulette = input().split()
roulette += roulette[:len(keyword) - 1]

# kmp 배열 만들기
kmp = [0 for _ in keyword]
j = 0
i = 1
for key in keyword[1:]:
    # j = 0인 경우, kmp[0] = 0 이라 초기화
    while j > 0 and key != keyword[j]:
        j = kmp[j - 1]
    if key == keyword[j]:
        j += 1
        kmp[i] = j
    i += 1
#print(kmp)
cnt = 0
j = 0
for i in range(N + len(keyword) - 1):
    #print(f'i : {i}, j : {j}')
    while j > 0 and roulette[i] != keyword[j]:
        j = kmp[j - 1]
    if roulette[i] == keyword[j]:
        if j == len(keyword) - 1:
            cnt += 1
            j = kmp[j]
        else:
            j += 1
for i in range(2, cnt + 1):
    while cnt / i == int(cnt / i) and N / i == int(N / i):
        cnt = cnt // i
        N = N // i

print(f"{cnt}/{N}")