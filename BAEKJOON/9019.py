from collections import deque
N = int(input())

def buildnumstr(a):
    a = str(a)
    if len(a) < 4:
        for _ in range(4 - len(a)):
            a = "0" + a
    return a

for _ in range(N):
    start, end = map(int, input().split())
    # 2배, -1 만으로 자리수 맞추기
    fqueue = deque()
    fqueue.append(("", start))
    visited = [False for _ in range(10000)]
    visited[start] = True
    while True:
        (calcstr, num) = fqueue.popleft()
        if num == end:
            print(calcstr)
            break
        if not visited[num * 2 % 10000]:
            visited[num * 2 % 10000] = True
            fqueue.append((calcstr + "D", num * 2 % 10000))
        if num >= 1 and not visited[num - 1]:
            visited[num - 1] = True
            fqueue.append((calcstr + "S", num - 1))
        elif num == 0 and not visited[9999]:
            visited[9999] = True
            fqueue.append((calcstr + "S", 9999))
        if len(calcstr) < 2 or (calcstr[-2:] != "RR" and calcstr[-2:] != "LL"):
            if calcstr == "" or calcstr[len(calcstr) - 1] != "R":
                newnum = int(buildnumstr(num)[1:] + buildnumstr(num)[0])
                if not visited[newnum]:
                    visited[newnum] = True
                    fqueue.append((calcstr + "L", newnum))
            if calcstr == "" or calcstr[len(calcstr) - 1] != "L":
                newnum = int(buildnumstr(num)[3] + buildnumstr(num)[:3])
                if not visited[newnum]:
                    fqueue.append((calcstr + "R", newnum))