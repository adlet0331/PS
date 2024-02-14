Target = int(input())
breaknum = int(input())
buttons = [i for i in range(10)]
if breaknum != 0:
    for i in map(int, input().split(" ")):
        buttons.remove(i)

# buttons 안에 있는 숫자들로만 Target에 가장 가까운 숫자 만들기
# 자리별로 나누어서 해보는 아이디어
targetlist = [int(i) for i in str(Target)]
maxdigit = len(targetlist)

if Target == 100 or breaknum == 10:
    print(abs(100 - Target))
else:
    resultdigitlist = []
    for digitnum in range(maxdigit):
        cdigit = -1
        upFlag = 0
        # 8999 일때 8이 고장안남, 일단 넣기
        if targetlist[digitnum] in buttons:
            cdigit = targetlist[digitnum]
        # 이미 마지막 자리수 일 경우, 이미 해당 채널이 존재한다는 뜻임 break
        if digitnum == maxdigit - 1 and cdigit != -1:
            resultdigitlist.append(cdigit)
            break
        # 해당 자리수 말고 다른걸 했을 때 더 작을 수도 있으니 가장 가까운 위아래 자리수 찾기. -1이면 존재 X
        upcdigit = 0
        downcdigit = 10
        cnt = 1
        while upcdigit == 0 or downcdigit == 10:
            if downcdigit == 10 and targetlist[digitnum] - cnt in buttons:
                downcdigit = targetlist[digitnum] - cnt
            elif downcdigit == 10 and targetlist[digitnum] - cnt < 0:
                downcdigit = -1

            if upcdigit == 0 and targetlist[digitnum] + cnt in buttons:
                upcdigit = targetlist[digitnum] + cnt
            elif upcdigit == 0 and targetlist[digitnum] + cnt >= 10:
                upcdigit = -1
            cnt += 1
        # 마지막 자리수가 아니고 cdigit가 존재할 경우, 넣고 바로 다음으로
        if digitnum != maxdigit - 1 and cdigit != -1:
            resultdigitlist.append(cdigit)
            continue
        # 마지막 자리일 경우, 현재까지 다 같은것이였으므로 차이가 가장 적은거 넣기
        if digitnum == maxdigit - 1:
            if abs(upcdigit - targetlist[digitnum]) >= abs(downcdigit - targetlist[digitnum]) and downcdigit != -1:
                resultdigitlist.append(downcdigit)
            else:
                resultdigitlist.append(upcdigit)
            break
        # 마지막 자리수가 아님
        # cdigit vs upcdigit
        if cdigit != -1 and upcdigit != -1 and abs(upcdigit - cdigit) == 1:
            if targetlist[digitnum + 1] >= 5:
                resultdigitlist.append(upcdigit)
                break
        # cdigit vs downcdigit
        if cdigit != -1 and downcdigit != -1 and abs(downcdigit - cdigit) == 1:
            if targetlist[digitnum + 1] < 5:
                resultdigitlist.append(downcdigit)
                print(downcdigit)
                break
        # cdigit 존재 X 위가 나을지 아래가 나을지 판별
        if cdigit == -1:
            if downcdigit == -1:
                resultdigitlist.append(upcdigit)
                break
            elif upcdigit == -1:
                resultdigitlist.append(downcdigit)
                break
            # upcdigit, downcdigit 둘 다 존재
            else:
                # 먼저 가까운 쪽으로 설정
                if abs(upcdigit - targetlist[digitnum]) > abs(downcdigit - targetlist[digitnum]):
                    resultdigitlist.append(downcdigit)
                elif abs(upcdigit - targetlist[digitnum]) < abs(downcdigit - targetlist[digitnum]):
                    resultdigitlist.append(upcdigit)
                # 그래도 판별 안되면 다음 자리수 보고 판별
                elif targetlist[digitnum + 1] >= 5:
                    resultdigitlist.append(upcdigit)
                else:
                    resultdigitlist.append(downcdigit)
                break
    print(resultdigitlist)
    # resultdigitlist 가 꽉 차있으면 그냥 계산, 아니면 알맞게 채워주기
    if len(resultdigitlist) != maxdigit:
        rlen = len(resultdigitlist)
        if targetlist[rlen - 1] < resultdigitlist[rlen - 1]:
            for _ in range(maxdigit - rlen):
                resultdigitlist.append(buttons[0])
        elif targetlist[rlen - 1] > resultdigitlist[rlen - 1]:
            for _ in range(maxdigit - rlen):
                resultdigitlist.append(buttons[-1])
    result = 0
    print(buttons)
    print(resultdigitlist)
    for digitnum in range(maxdigit):
        result += resultdigitlist[digitnum] * (10 ** (maxdigit - digitnum - 1))
    # edge 케이스 : 한 자리 작은거 or 한자리 큰거
    cnt = min(maxdigit + abs(result - Target), abs(100 - Target))
    downmaxdigit = maxdigit - 1
    if downmaxdigit >= 1:
        result = 0
        for digitnum in range(downmaxdigit):
            result += 10 ** (downmaxdigit - digitnum - 1)
        result *= buttons[-1]
        cnt = min(cnt, downmaxdigit + abs(result - Target))
    upmaxdigit = maxdigit + 1
    if upmaxdigit < 7:
        result = 0
        if 0 in buttons and len(buttons) > 1:
            result = buttons[1] * (10 ** (upmaxdigit - 1))
        else:
            for digitnum in range(maxdigit):
                result += 10 ** (upmaxdigit - digitnum - 1)
            result *= buttons[0]
        cnt = min(cnt, upmaxdigit + abs(result - Target))
    print(cnt)