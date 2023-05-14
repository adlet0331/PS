"""
하나하나씩 일일히 계산하려고 해서 시간초과 당함

n번째 날, 얼마나 태어나는지, 얼마나 죽는지, 얼마나 생산 가능한지
계산해보자
"""

a, b, d, N = map(int, input().split(" "))
cnt_list = list([1])
born_list = list([1] + [0 for _ in range(a-1)] + [1 for _ in range(b-a)])
for _ in range(N - b + 1):
    born_list.append(0)

for day in range(1, N + 1):
    for i in range(a, b):
        if day + i > N:
            break
        born_list[day + i] += born_list[day] 
        born_list[day + i] %= 1000

    die_index = day - d
    cnt_list.append((cnt_list[day-1] + born_list[day] - (0 if die_index < 0 else born_list[die_index])) % 1000) 
    #print(day, today_born_num, today_die_num)

print(cnt_list[N])