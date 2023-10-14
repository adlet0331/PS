# KMP 알고리즘

str = input()
keyword = input()
snum = len(str)
knum = len(keyword)

sindexlist = [0 for _ in range(knum)]
# j : prefix와 suffix 일치 최대 길이
j = 0
for i in range(1, knum):
    # prefix랑 suffix 일치 X 하다면 같을 때 까지 j 회귀
    while j > 0 and keyword[i] != keyword[j]:
        j = sindexlist[j - 1]
    
    # 이번에 추가된 문자열이 같다면 j 값 하나 추가
    if keyword[i] == keyword[j]:
        j += 1
        sindexlist[i] = j

# sindexlist 사용해서 찾기
cnt = 0
answerlist = []
findex = 0
for index in range(0, snum):
    #print(findex)
    # 다를 경우 : findex 최적화 된 방법으로 옮기기
    while findex > 0 and str[index] != keyword[findex]:
        findex = sindexlist[findex - 1]
    # 같을 경우: 평범하게 정답 판별 후 findex += 1
    if str[index] == keyword[findex]:
        if findex == knum - 1:
            cnt += 1
            answerlist.append(index - knum + 1)
            findex = sindexlist[findex]
        else:
            findex += 1

print(cnt)
for answer in answerlist:
    print(answer + 1, end = ' ')