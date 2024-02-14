x, y, w, h = map(int, input().split(" "))

# 0,0 - w, h
# 현재 위치 x, y

print(min(x, y, abs(x-w), abs(y-h)))