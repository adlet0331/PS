T = int(input())

# 조 좌표 x1,y1 백 좌표 x2,y2
# 조부터 마린 거리 r1, 백부터 마린 거리 r2
# 류가 있을 수 있는 좌표의 수

# 사이 거리 vs 거리의 합 / 차 비교하면 됨

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        if r1 != r2:
            print(0)
        continue
    
    brange_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    rsum_sq = (r1 + r2) ** 2
    rdif_sq = abs(r1 - r2) ** 2
    #print(brange_sq, rsum_sq)
    if rdif_sq < brange_sq and brange_sq < rsum_sq:
        print(2)
    elif brange_sq == rsum_sq or brange_sq == rdif_sq:
        print(1)
    else:
        print(0)