# 간단한 체스 NxN에 퀸을 서로 못 잡게 놓을 수 있는 경우의 수
# 규칙을 못찾겠다 그냥 백트래킹 써라! 
# 시간제한 10초에 메모라 128MB, N 이 최대 15다... 백트래킹이 맞는것 같네요

N = int(input())

# Check Every number of cases
def check_enc(curr_row, filled_arr):
    cnt = 0
    # (curr_col, curr_row) - 모든 curr_col 가능한지 체크
    for curr_col in range(N):
        # Check if index is valid
        vFlag = True
        for row in range(curr_row):
            col = filled_arr[row]
            # 가로세로
            if row == curr_row or col == curr_col:
                vFlag = False
                break
            # 대각선
            if curr_col - curr_row == col - row or curr_col + curr_row == row + col:
                vFlag = False
                break
        if not vFlag:
            continue
        if curr_row + 1 == N:
            cnt += 1
        else:
            copied_filled_arr = filled_arr.copy()
            copied_filled_arr[curr_row] = curr_col
            cnt += check_enc(curr_row + 1, copied_filled_arr)
    return cnt

dparr = [-1 for _ in range(N)]
print(check_enc(0, dparr))
