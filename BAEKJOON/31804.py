from collections import deque

a, b = map(int, input().split())

dq = deque()
dq.append((a, 0, False))

checked = [[False, False] for _ in range(b + 1)]
checked[a][0] = True

while True:
    (num, cnt, channeled) = dq.popleft()
    # print(num, cnt, channeled)
    if num + 1 == b or num * 2 == b or (not channeled and num * 10 == b):
        print(cnt + 1)
        break
    channelednum = 1 if channeled else 0
    if num + 1 < b and not checked[num + 1][channelednum]:
        checked[num + 1][channelednum] = True
        dq.append((num + 1, cnt + 1, channeled))
    if num * 2 < b and not checked[num * 2][channelednum]:
        checked[num * 2][channelednum] = True
        dq.append((num * 2, cnt + 1, channeled))
    if not channeled and num * 10 < b and not checked[num * 10][channelednum]:
        checked[num * 10][channelednum] = True
        dq.append((num * 10, cnt + 1, True))