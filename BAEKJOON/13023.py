"""
A - B - C - D - E
이렇게 이어진 친구 관계가 필요

DFS 사용하기
"""

N, M = map(int, input().split(" "))
routes = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    routes[a].append(b)
    routes[b].append(a)

def dfs(index, contained_list, cnt = 1):
    global routes
    result = False
    for next_node in routes[index]:
        if next_node in contained_list:
            continue
        if cnt == 4:
            return True
        result = dfs(next_node, contained_list + [next_node], cnt + 1)
        if result:
            return True
    return False

isfound = False
for i in range(N):
    isfound = dfs(i, [i])
    if isfound:
        break
print(int(isfound))