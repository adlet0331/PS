data = []
for _ in range(9):
    data.append(list(map(int, input().split())))
# row[a][b] a번째 행에 b라는 숫자가 채워져 있는지?
row_checklist = [[False for _ in range(10)] for _ in range(9)]
# col[a][b] a번째 열에 b라는 숫자가 채워져 있는지?
col_checklist = [[False for _ in range(10)] for _ in range(9)]
'''
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
'''
# (x,y) 점은 x//3 * 3 + y//3 square 안에 포함되어 있음 
square_checklist = [[False for _ in range(10)] for _ in range(9)]
def getsquarenum(x, y):
    return x // 3 * 3 + y // 3
for row in range(9):
    for col in range(9):
        num = data[row][col]
        if num == 0:
            continue
        row_checklist[row][num] = True
        col_checklist[col][num] = True
        square_checklist[getsquarenum(row, col)][num] = True
score = 0
def sdq(cnt):
    global score
    score += 1
    if cnt == 81:
        return True
    row = cnt // 9
    col = cnt % 9
    if data[row][col] != 0:
        return sdq(cnt + 1)
    for i in range(1, 10):
        if not row_checklist[row][i] and not col_checklist[col][i] and not square_checklist[getsquarenum(row, col)][i]:
            row_checklist[row][i] = True
            col_checklist[col][i] = True
            square_checklist[getsquarenum(row, col)][i] = True
            if sdq(cnt + 1):
                data[row][col] = i
                return True
            row_checklist[row][i] = False
            col_checklist[col][i] = False
            square_checklist[getsquarenum(row, col)][i] = False
    return False

sdq(0)
#for line in data:
#    print(*line, sep=" ")
print(score)