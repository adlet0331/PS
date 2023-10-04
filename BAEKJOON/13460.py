from collections import deque

row, column = map(int, input().split())
map_list = []
RCoordinate = [-1, -1]
BCoordinate = [-1, -1]
for r in range(row):
    input_str = input()
    map_list.append(input_str)
    if 'R' in input_str:
        RCoordinate = [r, input_str.index('R')]
    if 'B' in input_str:
        BCoordinate = [r, input_str.index('B')]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
find_deque = deque()
find_deque.append((RCoordinate, BCoordinate, 0))
game_success = False
success_cnt = -1
while len(find_deque) > 0:
    Rcoor, Bcoor, cnt = find_deque.popleft()
    if cnt > 9:
        continue
    for direction in directions:
        movex = direction[0]
        movey = direction[1]

        Ry = Rcoor[0]
        Rx = Rcoor[1]
        By = Bcoor[0]
        Bx = Bcoor[1]
        # direction으로 기울였을 때 움직여지지 않음 계산 X 
        if (map_list[Ry + movey][Rx + movex] == '#' and  map_list[By + movey][Bx + movex] == '#') or (Ry + movey == By and Rx + movex == Bx and map_list[By + movey][Bx + movex] == '#') or (map_list[Ry + movey][Rx + movex] == '#' and By + movey == Ry and Bx + movex == Rx):
            continue
        
        # 구멍에 빠지는지 판별, 안 빠지면 최종 위치로 이동 
        R_in_hole = False
        B_in_hole = False
        R_stop = False
        B_stop = False
        while True:
            if map_list[Ry][Rx] == 'O':
                R_in_hole = True
            if map_list[By][Bx] == 'O':
                B_in_hole = True
            
            if not R_in_hole and not R_stop:
                if map_list[Ry + movey][Rx + movex] == '#':
                    R_stop = True
                if not B_in_hole and (B_stop or map_list[By + movey][Bx + movex] == '#') and By == Ry + movey and Bx == Rx + movex:
                    R_stop = True
                if not R_stop:
                    Rx += movex
                    Ry += movey

            if not B_in_hole and not B_stop:
                if map_list[By + movey][Bx + movex] == '#':
                    B_stop = True
                if not R_in_hole and (R_stop or map_list[Ry + movey][Rx + movex] == '#') and Ry == By + movey and Rx == Bx + movex:
                    B_stop = True
                if not B_stop:
                    Bx += movex
                    By += movey
            
            if (R_stop or R_in_hole) and (B_stop or B_in_hole):
                break

        # 성공했는지 판별
        if R_in_hole and not B_in_hole:
            game_success = True
            success_cnt = cnt + 1
            break
        
        #실패시 다음 것 넣기
        if B_in_hole:
            continue
        find_deque.append(([Ry, Rx], [By, Bx], cnt + 1))

    if game_success:
        break

print(success_cnt)