# 하노이 탑 일일이 움직이는 거 찍으면 됨
import sys
print = sys.stdout.write

N = int(input())
def move(start, end, size):
    if size == 1:
        print(f"{start} {end}\n")
    else:
        last = 6 - start - end
        move(start, last, size - 1)
        print(f"{start} {end}\n")
        move(last, end, size - 1)

print(str(2 ** N - 1))
print('\n')
move(1, 3, N)