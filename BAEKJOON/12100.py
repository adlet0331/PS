N = int(input())

gmap = list()
for _ in range(N):
    gmap.append(list(map(int, input().split())))

brute_force = []
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            for i4 in range(4):
                for i5 in range(4):
                    brute_force.append(str(i1) + str(i2) + str(i3) + str(i4) + str(i5))

def swip_diagonal(gmap):
    n = len(gmap)
    new_gmap = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_gmap[i][j] = gmap[j][i]
    gmap = new_gmap

def swip_horizontal(gmap):
    for li in gmap:
        li.reverse()

directions = [[True, True], [True, False], [False, True], [False, False]]
mnum = 2
for dirs in brute_force:
    game_map = gmap.copy()
    for i in range(5):
        dir_index = int(dirs[i])
        if directions[dir_index][0]:
            swip_diagonal(game_map)

        if directions[dir_index][1]:
            swip_horizontal(game_map)
        
        # 2048 처리
        for index in range(N):
            nums_list = []
            aflag = False
            for el in game_map[index]:
                if el == 0:
                    continue
                if nums_list and nums_list[-1] == el and not aflag:
                    nums_list[-1]*= 2
                    aflag = True
                else:
                    nums_list.append(el)
                    aflag = False
                    
            for _ in range(N - len(nums_list)):
                nums_list.append(0)
            game_map[index] = nums_list

        if directions[dir_index][1]:
            swip_horizontal(game_map)
        

        if directions[dir_index][0]:
            swip_diagonal(game_map)

    for li in game_map:
        for num in li:
            mnum = num if num > mnum else mnum

print(mnum)