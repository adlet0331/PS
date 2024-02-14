Target = int(input())
breaknum = int(input())
buttons = [i for i in range(10)]
if breaknum != 0:
    for i in map(int, input().split(" ")):
        buttons.remove(i)

# 1,000,000 까지 이진 탐색
result = 1000001
for num in range(0, 1000000):
    # check
    flag = False
    for i in str(num):
        if int(i) not in buttons:
            flag = True
            break
    if flag:
        continue

    cnt = len(str(num)) + abs(Target - num)
    if result > cnt:
        result = cnt
print(min(result, abs(Target - 100)))