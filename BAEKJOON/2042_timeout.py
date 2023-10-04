N, M, K = map(int, input().split())
num_list = [0]
for i in range(N):
    num_list.append(int(input()))
c_list = []
sum_list = []
for index in range(M + K):
    isChange, num1, num2 = map(int, input().split())
    if isChange == 1:
        c_list.append((num1, num2, index))
    else:
        sum = 0
        for i in range(num1, num2 + 1):
            sum += num_list[i]
        sum_list.append([num1, num2, sum, index])
for change_node in c_list:
    (index, change_num, i) = change_node
    num = num_list[index]
    for sum_node in sum_list:
        [snum, enum, sum, j] = sum_node
        if i > j:
            continue
        if snum <= index and index <= enum:
            sum_node[2] += (change_num - num)
for sum_node in sum_list:
    print(sum_node[2])