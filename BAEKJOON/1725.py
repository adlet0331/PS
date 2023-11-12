N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

def find_max_histogram(start, end):
    if end - start <= 1:
        return max(min(arr[start], arr[end]) * (end - start + 1), arr[start], arr[end])
    smid = (start + end) // 2
    emid = (start + end) // 2 + 1
    minheight = min(arr[smid], arr[emid])
    maxval = max(arr[smid], arr[emid], 2 * min(arr[smid], arr[emid]))
    while smid != start and emid != end:
        if start != smid and emid != end:
            if arr[smid - 1] > arr[emid + 1]:
                smid -= 1
            else:
                emid += 1
        elif start != smid and emid == end:
            smid -= 1
        elif start == smid and emid != end:
            emid += 1
        else:
            break
        minheight = min(minheight, arr[smid], arr[emid])
        maxval = max(maxval, minheight * (emid - smid + 1))
    return max(maxval, find_max_histogram(start, (start + end) // 2), find_max_histogram((start + end) // 2 + 1, end))

print(find_max_histogram(0, N-1))