import sys
input = sys.stdin.readline

N = int(input())
requests = []
for _ in range(N):
    requests.append(list(int, map(input())))
# 1: 빼기, 2: 넣기 / 맛의 정도 / 개수
