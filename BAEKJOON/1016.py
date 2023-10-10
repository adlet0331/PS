min, max = map(int, input().split())
squaress = [True] * (max - min + 1)
# decimals = []
# 시간 복잡도로 인해.. 시간초과 뜸.
for i in range(2, int(max**0.5)+1):
    # isdecimal = True
    # for dec in decimals:
    #     if int(i / dec) == i / dec:
    #         isdecimal = False
    #         break
    # if not isdecimal:
    #     continue
    # decimals.append(i)
    temp = i ** 2
    index = int((min + temp - 1) / temp) * temp
    while index <= max:
        if squaress[index - min]:
            squaress[index - min] = False
        index += temp
result =0
for i in squaress:
    if i:
        result+=1
print(result)